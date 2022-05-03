using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using WebApplication3.Models.Entites;

namespace WebApplication3.Models.Context
{
    public class Ogrenci_isleriContext : DbContext
    {
        public Ogrenci_isleriContext() : base("Server=.;Database=Ogrenci_isleriDB;Trusted_Connection=true")
        {

        }

       
        public DbSet<Ogrenci> ogrencis { get; set; }

    }
}