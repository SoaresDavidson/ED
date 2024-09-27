#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

#define _ ios::sync_with_stdio(false); cin.tie(NULL);
#define pb push_back
#define endl '\n'
#define INF numeric_limits<long long>::max()

using namespace std;

vector<vector<long long>> dp;
vector<vector<bool>> vis;

long long solve(const vector<int>& v, int pos, int k) {
    if (k == 0) return 0; // Se já formamos k trios, o custo é 0
    if (pos >= v.size()) return INF; // Se não há mais bonecas, retorno infinito
    if (vis[pos][k]) return dp[pos][k]; // Se já calculado, retorna o valor

    vis[pos][k] = true; // Marca como visitado

    // Se não há bonecas suficientes para formar k trios
    if (3 * k > v.size() - pos) return dp[pos][k] = INF;

    // Caso onde não usamos a boneca atual
    long long result = solve(v, pos + 1, k);

    // Caso onde usamos a boneca atual como a menor de um trio
    if (pos + 1 < v.size() && k > 0) {
        result = min(result, (long long)(v[pos + 1] - v[pos]) * (v[pos + 1] - v[pos]) + solve(v, pos + 2, k - 1));
    }

    dp[pos][k] = result;
    return result;
}

int main() {_
    int n, k;
    cin >> n >> k;
    vector<int> v(n);

    for (int i = 0; i < n; ++i) cin >> v[i];
    
    sort(v.begin(), v.end());

    dp.resize(n, vector<long long>(k + 1, INF)); // Redimensiona dp
    vis.resize(n, vector<bool>(k + 1, false)); // Redimensiona vis

    // Inicializa dp e vis usando fill
    for (int i = 0; i < n; ++i) {
        fill(dp[i].begin(), dp[i].end(), INF);
        fill(vis[i].begin(), vis[i].end(), false);
    }

    cout << solve(v, 0, k) << endl;
    return 0;
}
