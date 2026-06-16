from risk_engine import get_risk_scores
from risk_storage import (
    create_risk_table,
    save_risk_score
)

create_risk_table()

scores = get_risk_scores()

for user, score in scores.items():

    save_risk_score(
        user,
        score
    )

print("Risk Scores Saved")