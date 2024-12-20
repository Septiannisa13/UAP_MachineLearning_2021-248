import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.pipeline import make_pipeline
import torch  # Ensure PyTorch is imported for TabNet
from pytorch_tabnet.tab_model import TabNetClassifier
import os  # To handle directory creation

def app():
    st.header("🤖 Klasifikasi Data")
    
    if 'data' in st.session_state:
        data = st.session_state['data']

        # Pilih fitur dan target
        st.sidebar.header("Pengaturan Klasifikasi")
        feature_columns = st.sidebar.multiselect(
            "Pilih Kolom Fitur:", options=data.columns, default=data.columns[:-1]
        )
        target_column = st.sidebar.selectbox("Pilih Kolom Target:", options=[data.columns[-1]])

        # Pilih model untuk klasifikasi
        model_algorithm = st.sidebar.selectbox(
            "Pilih Algoritma Model:", 
            options=["Logistic Regression", "Decision Tree", "Random Forest", "SVM", "Neural Network", "TabNet"]
        )

        if feature_columns and target_column:
            X = data[feature_columns]
            y = data[target_column]

            # Preprocessing
            label_enc = LabelEncoder()
            y = label_enc.fit_transform(y)

            # Separate numeric and non-numeric columns
            numeric_columns = X.select_dtypes(include=['number']).columns
            categorical_columns = X.select_dtypes(exclude=['number']).columns

            # Handle missing values in numeric columns
            imputer = SimpleImputer(strategy='mean')
            X[numeric_columns] = imputer.fit_transform(X[numeric_columns])

            # Handle categorical columns (if any) by encoding them
            for col in categorical_columns:
                X[col] = label_enc.fit_transform(X[col].astype(str))  # Convert to string if necessary

            # Scale numeric features
            scaler = StandardScaler()
            X[numeric_columns] = scaler.fit_transform(X[numeric_columns])

            # Train-Test Split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize and train selected model
            if model_algorithm == "Logistic Regression":
                model = LogisticRegression(random_state=42)
            elif model_algorithm == "Decision Tree":
                model = DecisionTreeClassifier(random_state=42)
            elif model_algorithm == "Random Forest":
                model = RandomForestClassifier(random_state=42)
            elif model_algorithm == "SVM":
                model = LinearSVC(random_state=42)  # Faster alternative to SVC
            elif model_algorithm == "Neural Network":
                model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
            elif model_algorithm == "TabNet":
                model = TabNetClassifier(
                    n_d=8, n_a=8, n_steps=3,
                    gamma=1.3, lambda_sparse=1e-4,
                    optimizer_fn=torch.optim.Adam,
                    optimizer_params=dict(lr=2e-2),
                    verbose=0
                )

            # Convert data to NumPy arrays for TabNet
            if model_algorithm == "TabNet":
                X_train_values = X_train.values
                X_test_values = X_test.values
                
                # Fit TabNet model
                model.fit(
                    X_train_values, y_train,
                    eval_set=[(X_test_values, y_test)],
                    eval_metric=['accuracy'],
                    max_epochs=50,  # Reduced for faster execution
                    patience=10,
                    batch_size=128,  # Use larger batch sizes
                    virtual_batch_size=64
                )
                predictions = model.predict(X_test_values)
            else:
                # For other models
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)

            st.success(f"Akurasi Model ({model_algorithm}): {accuracy:.2f}")
            st.write("Hasil Prediksi:") 
            st.write(predictions)
            
            # Confusion Matrix
            st.subheader("Confusion Matrix")
            cm = confusion_matrix(y_test, predictions)
            fig, ax = plt.subplots()
            ConfusionMatrixDisplay(cm).plot(ax=ax)
            st.pyplot(fig)

            # Classification Report
            st.subheader("Classification Report")
            report = classification_report(y_test, predictions, output_dict=True)
            st.dataframe(pd.DataFrame(report).transpose())

            # Save the model and X_test to session_state
            st.session_state['model'] = model
            st.session_state['X_test'] = X_test  # Save X_test

            # Ensure the model directory exists
            model_path = "D:/Machine Learning/UAP/src/model/my_model.joblib"
            if not os.path.exists(os.path.dirname(model_path)):
                os.makedirs(os.path.dirname(model_path))

            # Save model
            if model_algorithm == "TabNet":
                model.save_model(model_path.replace(".joblib", ""))  # Save TabNet model using its own method
            else:
                joblib.dump(model, model_path)  # Save other models using joblib

            st.success(f"Model disimpan sebagai '{model_path}'.")

        else:
            st.warning("Pilih kolom fitur dan target terlebih dahulu.")
    else:
        st.warning("Silakan unggah data terlebih dahulu di menu 'Unggah Data'.")
