from src import data_loader, preprocessing, feature_engineering, model, evaluate, utils

if __name__ == "__main__":
    utils.ensure_dirs()
    df = data_loader.load_data()
    df_clean = preprocessing.clean_data(df)
    features = feature_engineering.select_features(df_clean)
    features_scaled = feature_engineering.scale_features(features)
    trained_model = model.train_kmeans(features_scaled)
    evaluate.evaluate_model(features_scaled, trained_model)
    evaluate.visualize_clusters(features_scaled, trained_model)