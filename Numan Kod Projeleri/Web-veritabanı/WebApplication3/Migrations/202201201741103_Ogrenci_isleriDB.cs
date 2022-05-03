namespace WebApplication3.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class Ogrenci_isleriDB : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Ogrencis",
                c => new
                    {
                        ogr_id = c.Int(nullable: false, identity: true),
                        ogr_no = c.String(),
                        tc_no = c.String(),
                        ad = c.String(),
                        soyad = c.String(),
                        dogumTarihi = c.DateTime(nullable: false),
                        dogumYeri = c.String(),
                        notu = c.Int(nullable: false),
                    })
                .PrimaryKey(t => t.ogr_id);
            
        }
        
        public override void Down()
        {
            DropTable("dbo.Ogrencis");
        }
    }
}
