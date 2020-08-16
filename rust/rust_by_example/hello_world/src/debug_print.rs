/* Rust By Example - Print Debug 1.2.1 */

// This structure cannot be printed either with `fmt::Display` or
// with `fmt::Debug`.
#[allow(dead_code)]
struct UnPrintable(i32);

// The `derive` attribute automatically creates the implementation
// required to make this `struct` printable with `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);

// Derive the `fmt::Debug` implementation for `Structure`. `Structure`
// is a structure which contains a single `i32`.
#[derive(Debug)]
struct Structure(i32);

#[derive(Debug)]
struct Person<'a> {
    name: &'a str,
    age: u8
}

// Put a `Structure` inside of the structure `Deep`. Make it printable
// also.
#[derive(Debug)]
struct Deep(Structure);

#[allow(dead_code)]
pub fn run() {
    // Printing with `{:?}` is similar to with `{}`.
    println!("{:?} months in a year.", 12);
    println!("{1:?} {0:?} is the {actor:?} name.",
             "Slater",
             "Christian",
             actor="actor's");

    // `Structure` is printable!
    println!("Now {:?} will print!", Structure(3));

    // The problem with `derive` is there is no control over how
    // the results look. What if I want this to just show a `7`?
    println!("Now {:?} will print!", Deep(Structure(7)));

    // Pretty print
    let name = "Peter";
    let age = 27;
    let peter = Person { name, age };

    println!("{:#?}", peter);
}
