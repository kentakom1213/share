#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print_vector(vector<T>& vec) {
  cout << "[ ";
  for (int i = 0; i < vec.size(); i++) {
    if (i < vec.size() - 1) cout << vec.at(i) << " ";
    else cout << vec.at(i);
  }
  cout << " ]" << endl;
}

vector<string> get_permutations(string input) {
  if (input.size() == 1) return {input};
  else {
    vector<string> result;
    for (int i = 0; i < input.size(); i++) {
      char choice = input[i];

      string rest = "";
      for (int j = 0; j < input.size(); j++) {
        if (j != i) rest.push_back(input[j]);
      }

      vector<string> rest_perms = get_permutations(rest);
      for (int k = 0; k < rest_perms.size(); k++) {
        string added = choice + rest_perms[k];
        result.push_back(added);
      }
    }
    return result;
  }
}

int main() {
  string in_str;
  cin >> in_str;
  vector<string> perm = get_permutations(in_str);
  print_vector(perm);
  cout << perm.size() << endl;
}
