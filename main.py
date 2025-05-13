from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Parlay-GPT Back-End",
              description="Odds, stats, and probability endpoints",
              version="1.0.0")


# ====   Schemas   ============================================================
class Leg(BaseModel):
    selection: str
    odds: float


class ProbRequest(BaseModel):
    legs: List[Leg]


# ====   Routes   =============================================================

@app.get("/odds")
def get_odds(sport: str, market: str, book: str):
    """Return hard-coded sample odds until you plug in a real API."""
    return {
        "sport": sport,
        "market": market,
        "book": book,
        "odds": [
            {"selection": "Trea Turner 1+ hit", "price": 1.35},
            {"selection": "Kyle Schwarber 1+ hit", "price": 1.60},
        ],
    }


@app.get("/stats")
def get_stats(entity: str, stat_type: str, lookback: str = "14d"):
    return {
        "entity": entity,
        "stat_type": stat_type,
        "lookback": lookback,
        "stats": {"sample": "pending real feed"},
    }


@app.post("/prob")
def get_prob(payload: ProbRequest):
    # Just pretend every leg is 65 % and ignore correlation for now
    prob_per_leg = 0.65
    parlay_prob = prob_per_leg ** len(payload.legs)
    return {
        "legs": [
            {"selection": leg.selection,
             "prob": prob_per_leg,
             "edge_pct": 0.0,
             "grade": "yellow"}
            for leg in payload.legs
        ],
        "parlay_prob": parlay_prob,
        "ticket_grade": "yellow",
    }
