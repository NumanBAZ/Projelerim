using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

using WebApplication3.Models.Context;
using WebApplication3.Models.Entites;

namespace WebApplication3.Controllers
{
    public class girisController : Controller
    {
        Ogrenci_isleriContext db = new Ogrenci_isleriContext();
        public ActionResult Index()
        {
            var a = db.ogrencis.ToList();
            return View(a);
        }

        [HttpGet]
        public ActionResult Ekle()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Ekle(Ogrenci ogrenci)
        {
            try
            {
                db.ogrencis.Add(ogrenci);
                db.SaveChanges();
                TempData["Başarlı Mesaj"] = "Ekleme Yapıldı";

            }
            catch (Exception)
            {
                TempData["Hatalı Mesaj"] = "Ekleme Yapılamadı";
            }

            return RedirectToAction("Index");

        }

        public ActionResult Guncelle(int id)
        {


            var b = db.ogrencis.Find(id);
            if (b == null)
            {
                TempData["Hatalı Mesaj"] = "Kişi bulunamadı";
                return RedirectToAction("Index");
            }
            return View(b);
        }
        [HttpPost]
        public ActionResult Guncelle(Ogrenci ogrenci)
        {

            var a = db.ogrencis.Find(ogrenci.ogr_id);
            a.ogr_no = ogrenci.ogr_no;
            a.tc_no = ogrenci.tc_no;
            a.ad = ogrenci.ad;
            a.soyad = ogrenci.soyad;
            a.dogumTarihi = ogrenci.dogumTarihi;
            a.dogumYeri = ogrenci.dogumYeri;
            a.notu = ogrenci.notu;
            db.SaveChanges();
            TempData["Başarlı Mesaj"] = "Güncelleme başarılı";
            return RedirectToAction("Index");

        }

        public ActionResult Sil(int id)
        {
            var a = db.ogrencis.Find(id);
            if (a == null)
            {
                TempData["Hata Mesajı"] = "Silme başarısız";
                return RedirectToAction("Index");

            }
            db.ogrencis.Remove(a);
            db.SaveChanges();
            TempData["Başarlı Mesaj"] = "Silme Başarılı.";
            return RedirectToAction("Index");

        }
    }
}