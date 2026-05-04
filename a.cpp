#include <bits/stdc++.h>
#include <immintrin.h>

constexpr int SIZE = 100;

int main() {

  std::ofstream file("data/linearEx.txt");

  for (int i = 0; i < SIZE; i++) {
    file << i << '\n';
  }

  file.close();
  file.open("data/quadraticEx.txt");

  for (int i = 0; i < SIZE; i++) {
    file << (i * i) << '\n';
  }

  file.close();
  file.open("data/cubicEx.txt");

  for (int i = 0; i < SIZE; i++) {
    file << (i * i * i) << '\n';
  }
  file.close();
  file.open("data/logarithmicEx.txt");

  for (int i = 1; i < SIZE; i++) {
    file << (std::log(i)) << '\n';
  }

  file.close();
  file.open("data/exponentialEx.txt");

  for (int i = 0; i < SIZE; i++) {
    file << (std::exp(i)) << '\n';
  }
  file.close();
  return 0;
}
