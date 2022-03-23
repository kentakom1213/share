#include <bits/stdc++.h>
// #include <iostream.h>
using namespace std;


int sgn(string perm) {
  int count = 0;
  for (int i = 0; i < perm.size() - 1; i++) {
    for (int j = i + 1; j < perm.size(); j++) {
      if (perm[j] - perm[i] < 0) count++;
    }
  }
  return count % 2 ? -1 : 1;
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
  
  int c1 = 0, c_1 = 0;
  for (int i = 0; i < perm.size(); i++) {
    int sgn_ = sgn(perm[i]);
    if (sgn_ == 1) c1++;
    else c_1++;
    cout << perm[i] << ": " << sgn_ << endl;
  }
  printf("1: %d, -1: %d, sum= %d\n", c1, c_1, c1+c_1);
}
