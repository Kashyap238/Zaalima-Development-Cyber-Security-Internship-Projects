from risk_engine import get_risk_scores

def get_high_risk_users():

    risk_scores = get_risk_scores()

    high_risk = {}

    for user, score in risk_scores.items():

        if score >= 50:

            high_risk[user] = score

    return high_risk