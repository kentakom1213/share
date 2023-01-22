
use colored::Colorize;
use sudoku::sudoku::Sudoku;

fn main() {
    // 入力受け取り
    let mut sudoku = Sudoku::from_stdin();

    // 盤面の表示
    println!("\n{:^37}", "Problem".red().bold());
    sudoku.show();

    // 解を求める
    sudoku.solve();

    // 解の表示
    println!("\n{:^37}", "Answer".green().bold());
    sudoku.show();
}
