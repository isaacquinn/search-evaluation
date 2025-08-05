import json
import math

def load_results(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def precision_at_k(relevance, k=5):
    return sum(relevance[:k]) / k

def mrr(relevance_lists):
    reciprocal_ranks = []
    for relevance in relevance_lists:
        try:
            rank = relevance.index(1) + 1
            reciprocal_ranks.append(1 / rank)
        except ValueError:
            reciprocal_ranks.append(0)
    return sum(reciprocal_ranks) / len(relevance_lists)

def dcg(relevance, k=5):
    return relevance[0] + sum(rel / math.log2(i+1) for i, rel in enumerate(relevance[1:k], start=2))

def ndcg_at_k(relevance, k=5):
    dcg_val = dcg(relevance, k)
    ideal_relevance = sorted(relevance, reverse=True)
    idcg_val = dcg(ideal_relevance, k)
    return dcg_val / idcg_val if idcg_val != 0 else 0

def evaluate(results):
    precisions = []
    ndcgs = []
    relevance_lists = []
    
    for r in results:
        rel = r['relevance']
        precisions.append(precision_at_k(rel, 5))
        ndcgs.append(ndcg_at_k(rel, 5))
        relevance_lists.append(rel)

    print("Average Precision@5:", round(sum(precisions) / len(precisions), 4))
    print("Mean Reciprocal Rank (MRR):", round(mrr(relevance_lists), 4))
    print("Average NDCG@5:", round(sum(ndcgs) / len(ndcgs), 4))

if __name__ == "__main__":
    filepath = "results.json"  # assumes it's in the same folder
    results = load_results(filepath)
    evaluate(results)


# when ready to run the script...
# ensure that the folder (SearchEvaluation) from desktop has been opened in VSCode
# then use the following python script in the terminal... python evaluate_search_metrics.py
