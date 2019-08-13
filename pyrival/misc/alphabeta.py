class AlphaBetaNode:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children


def alphabeta(node, depth, alpha=float('-inf'), beta=float('+inf'), maximizingPlayer=True):
    if (depth == 0) or (node.children is None):
        return node.value
    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('+inf')
        for child in node.children:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
