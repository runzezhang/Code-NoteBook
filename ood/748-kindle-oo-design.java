// Design Kindle, which can support 3 type of book format: PDF, MOBI and EPUB.

// Consider using ENUM for book format.
// Consider using simple factory to create reader for each format.
// 设计一个可以打开三种文件格式的Kindle，文件格式分别为：PDF, MOBI , EPUB。

// 尝试使用 ENUM 处理文件格式。
// 尝试使用 simple factory 设计模式为每种格式创建用户。
// Have you met this question in a real interview?  
// Example
// Input:

// readBook("EPUB")
// readBook("PDF")
// readBook("MOBI")
// Output:

// Using EPUB reader, book content is: epub
// Using PDF reader, book content is: pdf
// Using MOBI reader, book content is: mobi

import java.util.ArrayList;
import java.util.List;

public class Kindle {
  private List<Book> books;
  private EBookReaderFactory readerFactory;

  public Kindle() {
    books = new ArrayList<>();
    readerFactory = new EBookReaderFactory();
  }

  public String readBook(Book book) throws Exception {
    EBookReader reader = readerFactory.createReader(book);
    if (reader == null) {
      throw new Exception("Can't read this format");
    }
    return reader.displayReaderType() + ", book content is: " + reader.readBook();
  }

  public void downloadBook(Book b) {
    books.add(b);
  }

  public void uploadBook(Book b) {
    books.add(b);
  }

  public void deleteBook(Book b) {
    books.remove(b);
  }
}

enum Format {
  EPUB("epub"), PDF("pdf"), MOBI("mobi");

  private String content;

  Format(String content) {
    this.content = content;
  }

  public String getContent() {
    return content;
  }
}

class Book {
  private Format format;

  public Book(Format format) {
    this.format = format;
  }

  public Format getFormat() {
    return format;
  }
}

abstract class EBookReader {

  protected Book book;

  public EBookReader(Book b) {
    this.book = b;
  }

  public abstract String readBook();

  public abstract String displayReaderType();
}

class EBookReaderFactory {

  public EBookReader createReader(Book b) {
    if (b.getFormat() == Format.EPUB) {
      return new EpubReader(b);
    } else if (b.getFormat() == Format.MOBI) {
      return new MobiReader(b);
    } else if (b.getFormat() == Format.PDF) {
      return new PdfReader(b);
    } else
      return null;
  }
}

class EpubReader extends EBookReader {

  public EpubReader(Book b) {
    super(b);
    // TODO Auto-generated constructor stub
  }

  @Override
  public String readBook() {
    // TODO Auto-generated method stub
    return book.getFormat().getContent();
  }

  @Override
  public String displayReaderType() {
    // TODO Auto-generated method stub
    return "Using EPUB reader";
  }
}

class MobiReader extends EBookReader {

  public MobiReader(Book b) {
    super(b);
    // TODO Auto-generated constructor stub
  }

  @Override
  public String readBook() {
    // TODO Auto-generated method stub
    return book.getFormat().getContent();
  }

  @Override
  public String displayReaderType() {
    // TODO Auto-generated method stub
    return "Using MOBI reader";
  }

}

class PdfReader extends EBookReader {

  public PdfReader(Book b) {
    super(b);
    // TODO Auto-generated constructor stub
  }

  @Override
  public String readBook() {
    // TODO Auto-generated method stub
    return book.getFormat().getContent();
  }

  @Override
  public String displayReaderType() {
    // TODO Auto-generated method stub
    return "Using PDF reader";
  }
}