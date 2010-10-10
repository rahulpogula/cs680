# Install pysqlite
# Install Elixir
# Install SQLAlchemy

from elixir import *

metadata.bind = "sqlite:///movies.sqlite"
metadata.bind.echo = True

class Movie(Entity):
  title = Field( Unicode(30) )
  year  = Field( Integer )
  description = Field( UnicodeText )
  director = ManyToOne('Director')
  
  def __repr__(self):
    return '<Movie "%s" - %d>' % (self.title, self.year)

class Director(Entity):
  name = Field(Unicode(60))
  movies = OneToMany('Movie')
  
  def __repr__(self):
    return '<Director "%s">' % self.name

# If this script is called directly, it acts like a migration
if __name__ == '__main__':
  setup_all( True )