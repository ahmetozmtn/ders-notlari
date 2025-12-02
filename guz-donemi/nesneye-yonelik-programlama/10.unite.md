
# Metotlar ve Aşırı Yükleme 

C# programlamanın temel yapı taşlarından olan metotları, parametre yönetimini ve Nesneye Yönelik Programlamanın (NYP) önemli kavramlarından olan Metot Aşırı Yükleme (Overloading) ve Geçersiz Kılma (Overriding) konularını ele almaktadır.

## 1. Metotların Temel Yapısı

Metotlar, belirli bir işlemi gerçekleştiren ve tekrar tekrar kullanılabilen kod bloklarıdır. Kodun modüler olmasını ve tekrarın önlenmesini sağlarlar.

- **Tanımlama:** `[Erişim Belirteci] [Dönüş Tipi] [Metot Adı] (Parametreler)`
    
- **Void Metotlar:** Geriye bir değer döndürmeyen metotlardır. `return` ifadesi değer almadan kullanılabilir veya hiç kullanılmaz.
    
- **Static Metotlar:** Sınıftan nesne türetilmesine gerek kalmadan, sınıf ismiyle doğrudan çağrılabilen metotlardır.
    

## 2. Parametre Aktarım Yöntemleri

C#'ta metotlara veri gönderirken değişkenin türüne ve kullanılan anahtar kelimeye göre bellek yönetimi değişir.

### A. Değer ve Referans Türleri

- **Değer Türü (Value Type):** `int`, `double`, `bool` gibi türlerdir. Metoda gönderildiğinde **kopyası** oluşturulur. Metot içindeki değişiklik ana değişkeni etkilemez.
    
- **Referans Türü (Reference Type):** Sınıflar (`class`), diziler ve string gibi türlerdir. Metoda **bellek adresi** gönderilir. Metot içindeki değişiklik ana nesneyi değiştirir.
    

### B. `ref` ve `out` Anahtar Kelimeleri

Değer türlerinin de referans gibi davranmasını (orijinal verinin değişmesini) sağlamak için kullanılırlar.

- **`ref`:** Değişkenin metoda gönderilmeden önce **mutlaka ilk değerinin atanmış olması** gerekir.
    
- **`out`:** Değişkenin ilk değerinin olmasına gerek yoktur, ancak metodun içerisinde **mutlaka bir değer ataması yapılmalıdır**.
    

## 3. Metot Aşırı Yükleme (Method Overloading)

Aynı isme sahip fakat parametre yapısı (sayısı veya türü) farklı olan birden fazla metodun tanımlanmasıdır.

- **Amaç:** Kod okunabilirliğini ve esnekliği artırmaktır.
    
- **Kural:** Parametre imzası farklı olmalıdır. Sadece geri dönüş tipinin farklı olması aşırı yükleme sayılmaz ve hata verir.
    

## 4. Metot Geçersiz Kılma (Method Overriding)

Kalıtım alınan bir sınıftaki metodun, alt sınıfta (türetilen sınıf) yeniden yazılarak davranışının değiştirilmesidir.

- **Base Class (Temel Sınıf):** Metot `virtual` olarak işaretlenmelidir.
    
- **Derived Class (Alt Sınıf):** Metot `override` olarak işaretlenmelidir.
    

## 5. Değişken Sayıda Parametre (`params`)

Bir metoda kaç adet parametre gönderileceğinin bilinmediği durumlarda kullanılır.

- **Kural:** `params` anahtar kelimesi ile tanımlanır ve bir dizi (`array`) tipinde olmalıdır.
    
- **Kısıt:** Metodun parametre listesinde en sonda yer almalıdır ve sadece bir tane `params` kullanılabilir.
    

## 6. Özyinelemeli (Recursive) Metotlar

Bir metodun, belirli bir şart sağlanana kadar kendi kendisini çağırmasıdır. Genellikle matematiksel hesaplamalarda (Faktöriyel, Fibonacci vb.) kullanılır. Sonsuz döngüye girmemesi için mutlaka bir "durdurma koşulu" (base case) olmalıdır.

---

### Kod Örnekleri


#### Örnek 1: `ref` ve `out` Kullanımı


```csharp
class ParametreOrnekleri
{
    // ref: Değişkenin değeri metoda girmeden atanmış olmalı
    public static void SayiyiDegistir(ref int sayi)
    {
        sayi = 100; // Orijinal değişkeni değiştirir
    }

    // out: Değer metot içinde atanmak zorundadır
    public static void KisiOlustur(out string ad)
    {
        ad = "Ahmet"; // Dışarıya bu değeri fırlatır
    }
}

// Kullanım:
// int a = 5;
// ParametreOrnekleri.SayiyiDegistir(ref a); // a artık 100 olur.
// string isim;
// ParametreOrnekleri.KisiOlustur(out isim); // isim "Ahmet" olur.
```

#### Örnek 2: Aşırı Yükleme (Overloading)


```csharp
class Hesapla
{
    // İki tamsayıyı toplar
    public int Topla(int s1, int s2)
    {
        return s1 + s2;
    }

    // Üç tamsayıyı toplar (Aşırı yükleme)
    public int Topla(int s1, int s2, int s3)
    {
        return s1 + s2 + s3;
    }

    // İki ondalıklı sayıyı toplar (Aşırı yükleme)
    public double Topla(double s1, double s2)
    {
        return s1 + s2;
    }
}
```

#### Örnek 3: Geçersiz Kılma (Overriding)


```csharp
class Sekil
{
    // Alt sınıflar bu metodu ezebilir (virtual)
    public virtual void Ciz()
    {
        Console.WriteLine("Bir şekil çizildi.");
    }
}

class Daire : Sekil
{
    // Temel sınıftaki metodu geçersiz kılıyoruz (override)
    public override void Ciz()
    {
        Console.WriteLine("Daire çizildi.");
    }
}
```

#### Örnek 4: `params` ve Recursive (Faktöriyel)


```csharp
class OzelIslemler
{
    // Değişken sayıda parametre toplama
    public int CokluTopla(params int[] sayilar)
    {
        int toplam = 0;
        foreach (int sayi in sayilar)
        {
            toplam += sayi;
        }
        return toplam;
    }

    // Recursive Faktöriyel
    public int Faktoriyel(int n)
    {
        if (n <= 1) return 1; // Durdurma koşulu (Base case)
        return n * Faktoriyel(n - 1); // Kendini çağırma
    }
}

// Kullanım:
// OzelIslemler islem = new OzelIslemler();
// int sonuc = islem.CokluTopla(10, 20, 30, 40); // İstediğimiz kadar sayı gönderebiliriz.
// int fakt = islem.Faktoriyel(5); // 120
```


