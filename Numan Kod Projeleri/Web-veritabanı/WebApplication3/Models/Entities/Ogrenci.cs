using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using WebApplication3.Models.Entites;

namespace WebApplication3.Models.Entites
{
    public class Ogrenci
    {
        [Key]
        public int ogr_id { get; set; }

        public string ogr_no { get; set; }
        public string tc_no { get; set; }
        public string ad { get; set; }
        public string soyad { get; set; }
        public DateTime dogumTarihi { get; set; }
        public string dogumYeri { get; set; }

        public int notu { get; set; }
     


    }
}