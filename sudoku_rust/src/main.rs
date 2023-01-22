type Field = [[u8; 9]; 9];

#[derive(Debug, Clone)]
struct Sudoku {
    field: Field,
    answer: Field,
}

impl Sudoku {
    fn from_stdin() -> Self {
        let mut field = [[0_u8; 9]; 9];
        for i in 0..9 {
            let mut line = String::new();
            std::io::stdin().read_line(&mut line).ok();
            let mut itr = line.trim().split_whitespace();
            for j in 0..9 {
                field[i][j] = itr.next().unwrap().parse().unwrap();
            }
        }

        Sudoku { field, answer: [[0; 9]; 9] }
    }

    fn dfs(&mut self, cur: usize) {
        // すでに探索が終了している場合
        if self.answer[0][0] != 0 {
            return;
        }

        // 解がもとまった場合
        if cur == 81 {
            self.answer = self.field;
            return;
        }

        let (i, j) = (cur/9, cur%9);
        if self.field[i][j] == 0 {

            // 順に代入する
            for n in 1..=9 {
                // 代入した際に条件を満たすかどうか
                let mut is_ok = true;

                for t in 0..9 {
                    // --- 行 ---
                    is_ok &= self.field[i][t] != n;

                    // --- 列 ---
                    is_ok &= self.field[t][j] != n;

                    // --- ブロック ---
                    let (r, c) = (i/3*3 + t/3, j/3*3 + t%3);
                    is_ok &= self.field[r][c] != n;
                }

                // 条件を満たしているとき
                if is_ok {
                    self.field[i][j] = n;
                    self.dfs(cur + 1);
                    self.field[i][j] = 0;
                }
            }
        } else {
            self.dfs(cur + 1);
        }
    }

    fn show(field: Field) {
        println!("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓");
        for i in 0..9 {
            print!("┃ ");
            for j in 0..9 {
                let d = field[i][j];
                if d == 0 {
                    print!("*");
                } else {
                    print!("{}", d);
                }
                match (j % 9, j % 3) {
                    (8, _) => println!(" ┃"),
                    (_, 2) => print!(" ┃ "),
                    _ => print!(" │ "),
                }
            }
            match (i % 9, i % 3) {
                (8, _) => println!("┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛"),
                (_, 2) => println!("┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫"),
                _ => println!("┠───┼───┼───╂───┼───┼───╂───┼───┼───┨"),

            }
        }
    }
}

fn main() {
    let mut sudoku = Sudoku::from_stdin();
    sudoku.dfs(0);

    Sudoku::show(sudoku.answer);
}
