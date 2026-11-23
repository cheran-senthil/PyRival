// --- Compile & Debug Commands (Shell / Notes) ---
// Standard contest compile (C++20, O2 optimization):
// g++ -std=c++20 -O2 -Wall -Wextra solution.cpp -o solution
//
// Debug compile (address/UB sanitizers + debug symbols + bounds/asserts):
// g++ -std=c++20 -O2 -g -fsanitize=address,undefined -D_GLIBCXX_DEBUG solution.cpp -o debug
// Note: Remove -D_GLIBCXX_DEBUG if using PBDS tree with custom/heavy iterators or strict time limits.

// --- Pragmas (GCC / Clang Optimization) ---
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>
using namespace std;

// --- Fast I/O & File Redirection ---
void fast_io() {
    cin.sync_with_stdio(0);
    cin.tie(0);
    // Note: Avoid using cout.tie(0)
    // Use '\n' instead of endl (endl flushes the buffer and is slow).
}

void file_io() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

// --- Output Formatting & Floating Point Precision ---
void formatting_examples() {
    double val = 5.12399;
    cout << fixed << setprecision(4) << val << '\n';// 5.1240 (stays active for subsequent prints)

    int num = 42;
    cout << setw(5) << setfill('0') << num << '\n';// 00042 (resets width after one print)

    cerr << "Debug message\n";// Print to stderr
}

// --- Vectors, Sorting & Custom Comparators ---
void vector_and_sorting() {
    vector<int> v = {3, 1, 4, 1, 5, 9};
    sort(v.begin(), v.end());// Ascending: {1, 1, 3, 4, 5, 9}
    sort(v.rbegin(), v.rend());// Descending: {9, 5, 4, 3, 1, 1}
    reverse(v.begin(), v.end());// Reverse in-place

    // Remove duplicates from sorted vector
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());// {1, 3, 4, 5, 9}

    // Custom comparator with lambda (must define strict weak ordering: use <, never <=)
    vector<pair<int, int>> pts = {{2, 5}, {1, 8}, {2, 3}};
    sort(pts.begin(), pts.end(), [](const auto& a, const auto& b) {
        if (a.first != b.first) return a.first < b.first;// First ascending
        return a.second > b.second;// Second descending
    });// Result: {(1, 8), (2, 5), (2, 3)}
}

// --- Binary Search (lower_bound / upper_bound) ---
void binary_search_examples() {
    vector<int> arr = {1, 3, 3, 3, 5, 7};
    // First index where element >= 3 (equivalent to bisect_left)
    int lb = lower_bound(arr.begin(), arr.end(), 3) - arr.begin();// 1
    // First index where element > 3 (equivalent to bisect_right)
    int ub = upper_bound(arr.begin(), arr.end(), 3) - arr.begin();// 4
    int count_of_3 = ub - lb;// 3
}

// --- Set, Multiset & Unordered Set ---
void sets_examples() {
    set<int> s = {3, 1, 4, 1};// Sorted unique elements: {1, 3, 4}
    s.insert(2);// O(log N)
    s.erase(3);// O(log N)
    bool has_4 = s.count(4);// 1 (or s.contains(4) in C++20)
    int smallest = *s.begin();// 1
    int largest = *s.rbegin();// 4

    // Set binary search (ALWAYS use member functions, NOT std::lower_bound(s.begin(), ...))
    auto it = s.lower_bound(2);// Iterator to first element >= 2
    if (it != s.end()) cout << *it << '\n';

    // Multiset (allows duplicates)
    multiset<int> ms = {1, 3, 3, 5};
    ms.erase(3);// WARNING: Erases ALL occurrences of 3!
    ms.erase(ms.find(3));// Erases ONLY ONE occurrence of 3 (ensure it exists first)
    // WARNING: Avoid using .count(x) on multisets as it takes O(#x) time
    // See ordered_multiset if you want multiset with fast count

    // Custom comparator for std::set
    auto cmp = [](int a, int b) { return a > b; };
    set<int, decltype(cmp)> desc_set(cmp);
}

// --- K-th Order Statistics (GNU Policy-Based Data Structure) ---
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

// Ordered set of unique ints: supports find_by_order (k-th smallest, 0-indexed) and order_of_key (< x count)
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

// Ordered multiset trick: pair<value, unique_id> so duplicate values stay distinct
using ordered_multiset = tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>;

void pbds_example() {
    ordered_set<int> os;
    os.insert(10);
    os.insert(5);
    os.insert(20);

    int kth = *os.find_by_order(1);// 10 (0-indexed: 0->5, 1->10, 2->20); check it != os.end() if unsure
    int cnt_less = os.order_of_key(15);// 2 (number of elements strictly < 15)
    int cnt_less_or_eq = os.order_of_key(10 + 1);// 2 (number of elements <= 10 for ints)
    os.erase(10);// Erase by value (no-op if not present); also accepts iterator os.erase(os.find(10))

    // Multiset usage example (unique uid >= 0 per insert; INF > max uid)
    const int INF = 1e9;
    ordered_multiset oms; // Uses pair to get multiset functionality from a set
    int uid = 0;
    oms.insert({5, uid++});
    oms.insert({5, uid++});
    oms.insert({9, uid++});

    int cnt_lt_9 = oms.order_of_key({9, -1});// Strictly < 9 -> 2, O(log N)
    int cnt_leq_5 = oms.order_of_key({5, INF});// <= 5 -> 2, O(log N)
    int cnt_eq_5 = oms.order_of_key({5, INF}) - oms.order_of_key({5, -1});// Exact count of 5 -> 2, O(log N)
    int cnt_gt_5 = (int)oms.size() - oms.order_of_key({5, INF});// Strictly > 5 -> 1, O(log N)

    // Erase ONE occurrence of value 5 safely (avoid oms.erase({5, ...}) unless uid is known)
    auto it = oms.lower_bound({5, -1});
    if (it != oms.end() && it->first == 5) oms.erase(it);// Removes only one copy of 5
}


// --- Map & Unordered Map (Counter / defaultdict) ---
void maps_examples() {
    map<string, int> freq;// Sorted by key, O(log N)
    freq["apple"]++;// Auto-initializes to 0, then increments to 1
    freq["banana"] += 2;

    for (const auto& [key, val] : freq) {
        cout << key << ": " << val << '\n';
    }

    // Hash map: O(1) average, but vulnerable to anti-hash tests on Codeforces
    unordered_map<int, int> umap;
}

// --- Anti-Hash Protection (splitmix64 for unordered_map / unordered_set) ---
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15ULL;// Fixed golden-ratio constant
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();// Randomize per run
        return splitmix64(x + FIXED_RANDOM);
    }
};

void anti_hash_example() {
    unordered_map<long long, int, custom_hash> safe_map;// Resistant to collision hacks
    safe_map[1234567890123LL]++;
}

// --- Queue, Deque & Stack ---
void queue_stack_deque() {
    queue<int> q;// FIFO (for BFS)
    q.push(10);
    q.push(20);
    int front_val = q.front();// 10 (peek)
    q.pop();// Removes 10 (returns void!)

    stack<int> st;// LIFO
    st.push(10);
    int top_val = st.top();// 10
    st.pop();// Removes 10

    deque<int> dq;// Double-ended queue (0-1 BFS, sliding window)
    dq.push_front(1);
    dq.push_back(2);
    dq.pop_front();
    dq.pop_back();
}

// --- Priority Queue (Heap) ---
void priority_queue_examples() {
    // Max-heap by default
    priority_queue<int> max_pq;
    max_pq.push(3);
    max_pq.push(1);
    max_pq.push(5);
    int largest = max_pq.top();// 5
    max_pq.pop();// Removes 5

    // Min-heap syntax
    priority_queue<int, vector<int>, greater<int>> min_pq;
    min_pq.push(3);
    min_pq.push(1);
    int smallest = min_pq.top();// 1

    // Custom comparator for priority_queue (NOTE: logic is inverted vs std::sort; true means 'a' has LOWER priority)
    auto cmp = [](pair<int, int> a, pair<int, int> b) {
        return a.second > b.second;// Min-heap ordered by .second
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> custom_pq(cmp);
}

// --- Strings & Character Checks ---
void string_examples() {
    string s = "  hello world  ";
    string sub = s.substr(2, 5);// "hello" (start index, LENGTH - not end index!)
    size_t pos = s.find("world");// 8 (returns string::npos if not found)
    if (pos != string::npos) { /* found */ }

    int x = stoi("12345");// String to int (stoll for long long)
    string str_x = to_string(12345);// Number to string

    char c = 'b';
    bool is_alpha = isalpha(c);// Non-zero if letter
    bool is_digit = isdigit(c);// Non-zero if '0'-'9'
    char upper_c = toupper(c);// 'B'

    // Split string by whitespace using stringstream
    stringstream ss("  a   b  c ");
    string word;
    vector<string> tokens;
    while (ss >> word) tokens.push_back(word);// {"a", "b", "c"}
}

// --- Permutations & Combinatorics ---
void permutations_examples() {
    string s = "ABC";
    sort(s.begin(), s.end());// MUST be sorted first to visit all permutations
    do {
        cout << s << '\n';
    } while (next_permutation(s.begin(), s.end()));

    // Combinations (nCk) using a bitmask / selector vector
    int n = 4, k = 2;
    vector<int> sel(n, 0);
    fill(sel.end() - k, sel.end(), 1);// {0, 0, 1, 1}
    do {
        for (int i = 0; i < n; ++i) {
            if (sel[i]) cout << i << ' ';
        }
        cout << '\n';
    } while (next_permutation(sel.begin(), sel.end()));
}

// --- Bit Operations (C++20 <bit> & Builtins) ---
void bit_examples() {
    unsigned int x = 5;// 0b101
    int bits_needed = bit_width(x);// 3 (equivalent to Python's bit_length)
    int set_bits = popcount(x);// 2 (equivalent to Python's bit_count)
    int leading_zeros = countl_zero(x);
    int trailing_zeros = countr_zero(x);
    bool is_pow2 = has_single_bit(x);// false

    // GCC builtins (also work on signed long long with 'll' suffix)
    int pop_ll = __builtin_popcountll(5LL);// 2
    int ctz_ll = __builtin_ctzll(12LL);// 2 (trailing zeros; undefined for 0)
    int clz_ll = __builtin_clzll(5LL);// 61 (leading zeros in 64-bit; undefined for 0)
}

// --- Math, Limits & Division Tricks ---
void math_examples() {
    int g = gcd(24, 36);// 12 (<numeric>, C++17)
    int l = lcm(4, 6);// 12 (<numeric>, C++17)

    // Infinity constants (avoid overflow when adding inf + inf)
    const int INF = 1e9;
    const long long LINF = 1e18;
    int max_int = numeric_limits<int>::max();// 2147483647 (~2.14e9)

    // Integer division for positive a, b
    long long a = 7, b = 3;
    long long floor_div = a / b;// 2
    long long ceil_div = (a + b - 1) / b;// 3

    // 128-bit integer to avoid intermediate overflow in (a * b) % mod
    __int128 big = (__int128)1e18 * 1e18;
}

// --- Random Number Generation (Mersenne Twister) ---
void random_examples() {
    // Never use rand(); its range is too small and quality is poor
    mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

    long long r_int = uniform_int_distribution<long long>(1, 10)(rng);// [1, 10] inclusive
    double r_real = uniform_real_distribution<double>(1.0, 5.0)(rng);// [1.0, 5.0)

    vector<int> v = {1, 2, 3, 4, 5};
    shuffle(v.begin(), v.end(), rng);// Randomly shuffle vector
}

// --- Recursive Lambda (Memoization / DFS without global functions) ---
void recursive_lambda_example() {
    int n = 50;
    vector<long long> memo(n + 1, -1);

    auto fib = [&](auto& self, int x) -> long long {
        if (x < 2) return x;
        if (memo[x] != -1) return memo[x];
        return memo[x] = self(self, x - 1) + self(self, x - 2);
    };

    cout << fib(fib, 50) << '\n';
}

// --- Prime Sieve (Sieve of Eratosthenes) ---
vector<int> sieve(int limit) {
    vector<bool> is_prime(limit, true);
    if (limit > 0) is_prime[0] = false;
    if (limit > 1) is_prime[1] = false;
    for (int i = 2; i * i < limit; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j < limit; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> primes;
    for (int i = 2; i < limit; ++i) {
        if (is_prime[i]) primes.push_back(i);
    }
    return primes;
}

// --- Range-Based For Loops (For-Each) ---
void foreach_examples() {
    vector<int> v = {10, 20, 30};

    // Read-only by value (copies each element; good for primitives like int)
    for (int x : v) {
        cout << x << ' ';
    }

    // Read-only by const reference (avoids copying strings, vectors, structs)
    vector<string> words = {"alpha", "beta"};
    for (const auto& w : words) {
        cout << w << ' ';
    }

    // Modify elements in-place by reference
    for (auto& x : v) {
        x *= 2;// v becomes {20, 40, 60}
    }

    // Iterate over initializer list directly
    for (int d : {-1, 0, 1}) {
        cout << d << ' ';
    }
}

// --- Packing & Unpacking (pair, tuple, structured bindings) ---
void pack_unpack_examples() {
    // 1. Packing into pair and tuple
    pair<int, string> p = {1, "first"};// or make_pair(1, "first")
    tuple<int, int, string> t = {10, 20, "hi"};// or make_tuple(10, 20, "hi")

    // Access elements without unpacking
    int p_first = p.first;// 1
    string t_third = get<2>(t);// "hi" (0-indexed compile-time index)

    // 2. Unpacking with Structured Bindings (C++17+)
    auto [id, name] = p;// Copies values
    auto& [a, b, msg] = t;// References: modifying 'a' modifies 't'
    a = 99;// t is now {99, 20, "hi"}

    // Unpacking inside range-based for loops (maps, edge lists, coordinates)
    vector<pair<int, int>> edges = {{1, 2}, {2, 3}};
    for (const auto& [u, v] : edges) {
        cout << u << " -> " << v << '\n';
    }

    vector<tuple<int, int, long long>> weighted_edges = {{1, 2, 100LL}};
    for (auto [u, v, w] : weighted_edges) {
        cout << u << ' ' << v << ' ' << w << '\n';
    }

    // 3. Unpacking into existing variables with std::tie (also works with std::ignore)
    int x, y;
    tie(x, y) = make_pair(5, 10);// x = 5, y = 10
    tie(x, ignore) = make_pair(42, 99);// x = 42, second value discarded

    // Swap or cyclic shift using tie
    int c = 1, d = 2, e = 3;
    tie(c, d, e) = make_tuple(e, c, d);// c = 3, d = 1, e = 2

    // 4. Fixed-size std::array (supports structured bindings + lexicographical comparison)
    array<int, 3> pt = {1, 2, 3};
    auto [px, py, pz] = pt;
}
