import numpy as np

states = ["R", "P"]
pi = {"R": 0.5, "P": 0.5}
A = {"R": {"R": 0.6, "P": 0.4}, "P": {"R": 0.4, "P": 0.6}}
B = {
    "R": {"T": 0.2, "C": 0.3, "A": 0.2, "G": 0.3},
    "P": {"T": 0.3, "C": 0.2, "A": 0.3, "G": 0.2}
}
sequence = ["G", "G", "C", "A"]

def forward(sequence, states, pi, A, B):
    T = len(sequence)
    alpha = np.zeros((T, len(states)))
    c = np.zeros(T)  # scaling factors
    idx = {s:i for i,s in enumerate(states)}
    
    # Initialization
    for s in states:
        alpha[0, idx[s]] = pi[s] * B[s][sequence[0]]
    c[0] = 1.0 / np.sum(alpha[0,:])
    alpha[0,:] *= c[0]
    
    # Recursion
    for t in range(1, T):
        for j in states:
            sum_prev = sum(alpha[t-1, idx[i]] * A[i][j] for i in states)
            alpha[t, idx[j]] = sum_prev * B[j][sequence[t]]
        c[t] = 1.0 / np.sum(alpha[t,:])
        alpha[t,:] *= c[t]
    
    log_prob = -np.sum(np.log(c))
    return alpha, log_prob

def backward(sequence, states, A, B, c):
    T = len(sequence)
    beta = np.zeros((T, len(states)))
    idx = {s:i for i,s in enumerate(states)}
    
    # Initialization
    beta[T-1,:] = c[T-1]  # scaled
    
    # Recursion backwards
    for t in reversed(range(T-1)):
        for i in states:
            beta[t, idx[i]] = sum(
                A[i][j] * B[j][sequence[t+1]] * beta[t+1, idx[j]]
                for j in states
            )
        beta[t,:] *= c[t]
    return beta

# Run forward-backward
alpha, log_prob = forward(sequence, states, pi, A, B)
beta = backward(sequence, states, A, B, c=np.exp(-log_prob/len(sequence))*np.ones(len(sequence)))

print("Log probability of GGCA:", log_prob)
print("Scaled forward table:\n", alpha)
print("Scaled backward table:\n", beta)
