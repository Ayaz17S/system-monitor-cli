#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    long long total = 1LL * n * (n + 1) / 2; // Sum of 1 to n
    long long sum = 0;

    for (int i = 0; i < n - 1; ++i)
    {
        int num;
        cin >> num;
        sum += num;
    }

    cout << total - sum << endl; // Missing number
    return 0;
}
