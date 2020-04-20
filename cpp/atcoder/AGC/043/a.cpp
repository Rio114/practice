#include <bits/stdc++.h>
using namespace std;

int h, w;

void fill(vector<vector<char>> &board, vector<vector<bool>> &checked, int y, int x) {
  if (y < 0 || x < 0 || y >= h || x >= w) return;
  if (board.at(y).at(x) == '.') return;
  if (checked.at(y).at(x)) return;

  checked.at(y).at(x) = true;  // 既に調べているという状態に変えておく
  fill(board, checked, y    , x + 1);  // 右
  fill(board, checked, y + 1, x    );  // 下
}

bool check_connected(vector<vector<char>> &board) {
  vector<vector<bool>> checked(h, vector<bool>(w, false));

  // 陸地マスを1つ探す
  int y=0, x=0;

  /* 引数： 盤面, チェック二次元配列, y座標, x座標*/
  fill(board, checked, y, x);  // (y, x)から到達できるすべての陸地マスのcheckedをtrueにする

  bool ok = true;
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      if (board.at(i).at(j) == '.') {
        if (!checked.at(i).at(j)) {
          // 到達できていない陸地マスがある
          ok = false;
        }
      }
    }
  }
  return ok;
}


int main(){
    cin >> h >> w;
    vector<vector<char>> board(h, vector<char>(w));
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
        cin >> board.at(i).at(j);
        }
    }
    int i;

    while(1){
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
        if (board.at(y).at(x) == '.') continue;

        board.at(y).at(x) = '.';  // 埋め立てたと仮定する

        if (check_connected(board)) {
          cout << "YES" << endl;
          return 0;
        }

        board.at(y).at(x) = '#';  // 戻す
        }
      }
    }
}
