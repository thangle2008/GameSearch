# Helper functions

def score_to_star(score):
    """
    Convert a double score rating (0-100) to star rating (0-5)
    """
    return int(round(score / 20.0))