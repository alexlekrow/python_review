mod formatted_print;    // 1.2
mod debug_print;        // 1.2.1
mod display_print;      // 1.2.2
mod test_case;          // 1.2.2.1
mod formatting_print;   // 1.2.3

fn main() {
    formatted_print::run();
    debug_print::run();
    display_print::run();
    test_case::run();
    formatting_print::run();
}