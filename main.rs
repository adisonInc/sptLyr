use std::io;
use termion::{color, style};
use termion::screen::AlternateScreen;
use termion::raw::IntoRawMode;
use tui::Terminal;
use tui::backend::TermionBackend;
use tui::widgets::{Widget, Block, Borders, Sparkline, Paragraph, List, ListItem};
use tui::layout::{Layout, Constraint, Direction};
use std::{time, thread};
use std::fs::File;
use std::io::prelude::*;
use std::process::Command;
use std::path::Path;
use::std::fs;

fn main() -> Result<(), io::Error> {
    let stdout = io::stdout().into_raw_mode()?;
    let stdout = AlternateScreen::from(stdout);
    let backend = TermionBackend::new(stdout);
    let mut terminal = Terminal::new(backend)?;
   
    loop{
    let mut file = File::open("out.txt").expect("Unable to open the file");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Unable to read the file");
     
    let mut file2 = File::open("out2.txt").expect("Unable to open the file");
    let mut contents2 = String::new();
    file2.read_to_string(&mut contents2).expect("Unable to read the file");
     

    let mut fileTitle = File::open("title.txt").expect("Unable to open the file");
    let mut contentsTitle = String::new();
    fileTitle.read_to_string(&mut contentsTitle).expect("Unable to read the file");
     
    terminal.draw(|f| {
        let chunks = Layout::default()
            .direction(Direction::Horizontal)
            .margin(0)
            .constraints(
                [
                    
                    Constraint::Percentage(50),
                    Constraint::Percentage(50),
                ].as_ref()
            )
            .split(f.size());
        let items = [ListItem::new(contentsTitle.clone())];
        let items = [ListItem::new(contentsTitle.clone())];
        let list = List::new(items)
              .block(Block::default().title("Title").borders(Borders::ALL));
        let items = [ListItem::new(contents.clone())];
        let list = List::new(items)
              .block(Block::default().title("Lyrics").borders(Borders::ALL));
        f.render_widget(list, chunks[0]);
        let items = [ListItem::new(contents2.clone())];
        let list = List::new(items)
              .block(Block::default().title("Lyrics").borders(Borders::ALL));
        f.render_widget(list, chunks[1]);
    
    }
    );
    
  }
}


