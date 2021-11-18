import xgboost as xgb
from sklearn.pipeline import Pipeline  # type: ignore

regressor_pipe = Pipeline(
    [
        # ===== REGRESSION =====
        # Do the selected regression model
        (
            "XGB regression",
            xgb.XGBRegressor(
                base_score=0.5,
                booster="gbtree",
                colsample_bylevel=1,
                colsample_bynode=1,
                colsample_bytree=0.2,
                gamma=30.0,
                gpu_id=-1,
                importance_type="gain",
                interaction_constraints="",
                learning_rate=0.1,
                max_delta_step=0,
                max_depth=9,
                min_child_weight=5,
                missing=1,
                monotone_constraints="()",
                n_estimators=100,
                n_jobs=16,
                num_parallel_tree=1,
                random_state=0,
                reg_alpha=0,
                reg_lambda=1,
                scale_pos_weight=1,
                subsample=0.8,
                tree_method="exact",
                validate_parameters=1,
                verbosity=None,
            ),
        )
    ]
)
