// Week 14: CLI application (capstone)
//
// Build a command-line password generator using the clap library.
//
// The logic lives in generator.rs and validator.rs.
// Your job here is to wire up the CLI: parse arguments and call the right functions.
//
// Run: cargo test           (tests both the library logic and CLI behavior)
//      cargo run -- --help  (see the CLI interface once implemented)

#![allow(unused_variables, unused_imports)]

mod generator;
mod validator;

use clap::{Parser, Subcommand};
use generator::{generate_passphrase, generate_pin, generate_random};
use validator::{calculate_entropy, check_common_patterns, validate_strength};

/// A password generator CLI.
#[derive(Parser)]
#[command(name = "passgen", version, about = "Generate and validate passwords")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Generate a random password.
    Random {
        #[arg(short, long, default_value_t = 16)]
        length: usize,

        #[arg(short, long)]
        symbols: bool,
    },

    /// Generate a passphrase from random words.
    Passphrase {
        #[arg(short, long, default_value_t = 4)]
        words: usize,

        #[arg(short, long, default_value_t = '-')]
        separator: char,
    },

    /// Generate a numeric PIN.
    Pin {
        #[arg(short, long, default_value_t = 6)]
        length: usize,
    },

    /// Check the strength of a password.
    Validate { password: String },
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Commands::Random { length, symbols } => {
            let password = generate_random(length, symbols);
            let entropy = calculate_entropy(&password);

            println!("Generated password: {}", password);
            println!("Entropy: {:.2} bits", entropy);
        }

        Commands::Passphrase { words, separator } => {
            let passphrase = generate_passphrase(words, separator);

            println!("Generated passphrase: {}", passphrase);
        }

        Commands::Pin { length } => {
            let pin = generate_pin(length);

            println!("Generated PIN: {}", pin);
        }

        Commands::Validate { password } => {
            let strength = validate_strength(&password);
            let entropy = calculate_entropy(&password);

            println!("Password strength: {}", strength);
            println!("Entropy: {:.2} bits", entropy);

            if check_common_patterns(&password) {
                println!("Warning: This password uses a common or predictable pattern.");
            }
        }
    }
}
