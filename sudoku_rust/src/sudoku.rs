use colored::Colorize;

pub type Field = [[u8; 9]; 9];

#[derive(Debug, Clone)]
pub struct Sudoku {
    field: Field,
    answer: Field,
}

impl Sudoku {
    pub fn from_stdin() -> Self {
        let mut field = [[0_u8; 9]; 9];
        for i in 0..9 {
            let mut line = String::new();
            std::io::stdin().read_line(&mut line).ok();
            let mut itr = line.trim().split_whitespace();
            for j in 0..9 {
                field[i][j] = itr
                    .next()
                    .expect(&"[Error] 不正な入力です".red().to_string())
                    .parse()
                    .expect(&"[Error] 不正な入力です".red().to_string())
            }
        }

        Sudoku { field, answer: [[0; 9]; 9] }
    }

    /// ## solve
    /// 数独の解を求める（`Sudoku::dfs`のwrapper）
    pub fn solve(&mut self) {
        let field = self.field.clone();

        // DFSで解を求める
        self.dfs(0);
        self.field = field;
    }

    /// ## dfs
    /// 深さ優先探索により解を求める
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

    /// ## show
    /// 結果を整形して表示する
    pub fn show(&self) {
        println!("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓");
        for i in 0..9 {
            print!("┃ ");
            for j in 0..9 {
                match (self.field[i][j], self.answer[i][j]) {
                    (0, 0) => print!(" "),
                    (0, d) => print!("{}", d.to_string().green().bold()),
                    (d, _) => print!("{}", d),
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
