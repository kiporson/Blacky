# DIABLO BLACKHAT ENGINE

Sistem otomatisasi earning & stealth dengan modul AI dan dashboard visual.
Deploy-ready untuk Railway (Flask, .env, Procfile, ChartJS).

## Struktur
- `core/` : Proxy, Spoofer, Identity
- `earn/` : CPA, Affiliate, AI Rotator
- `defender/` : Anti-captcha, monitoring
- `stealth/` : Header & fingerprint cloaking
- `wallet_split/` : Withdraw dan mirror wallet
- `dashboard.py` : Visualisasi earnings (Chart.js)
- `ai_rotator.py` : Pemilihan offer CPA cerdas

## Menjalankan
```bash
python3 main.py
```

## Environment Variables
Siapkan file `.env` berdasarkan contoh `.env.example` dengan variabel berikut:

- `TELEGRAM_TOKEN` - token bot Telegram
- `TELEGRAM_CHAT_ID` - ID atau username chat tujuan
- `API_KEY` dan `SECRET_KEY` - kredensial aplikasi
- `MAIN_WALLET_ADDRESS` - alamat dompet utama untuk withdraw
- `PROXY_API_SOURCE` - endpoint daftar proxy (opsional)
- `BINANCE_API_KEY` dan `BINANCE_API_SECRET` - akses API Binance untuk withdraw
- `TRX_PRIVATE_KEY` - kunci pribadi saat menggunakan `withdraw_tron.py`

## Withdraw
Script penarikan tersedia untuk Binance dan TRX:

- Jalankan `python3 wallet_split/withdraw_binance.py` setelah mengatur `BINANCE_API_KEY` dan `BINANCE_API_SECRET`.
- Gunakan `python3 withdraw_tron.py` dan isi `TRX_PRIVATE_KEY` untuk penarikan TRX.
