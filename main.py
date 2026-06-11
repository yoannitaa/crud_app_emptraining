# ===================================
# Employee Training Inventory Application
# ===================================
# Developed by.
# JCDS - [33]
# Versi: 2.0 — Integrasi Database MySQL

# /************************************/

import mysql.connector
from mysql.connector import Error

# /===== Konfigurasi Database =====/
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # user MYSQL
    "password": '',          # pass MYSQL
    "database": "employee_training"
}

def get_connection():
    ## Membuat koneksi ke database MySQL.
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"[ERROR] Gagal koneksi ke database: {e}")
        return None


# /===== Feature Program =====/

# --- Menu ---

def main_menu():
    print("\n=== Inventory Training Karyawan Bank ABC ===\n")
    print("1. Report Data Training Karyawan")
    print("2. Menambahkan Data Training Karyawan")
    print("3. Mengubah Data Training Karyawan")
    print("4. Menghapus Data Training Karyawan")
    print("5. Exit")
    input_mainmenu = input("Silahkan Pilih Menu Utama [1-5]: ")
    return input_mainmenu

def view_submenuread():
    print("\n~~~ Report Data Training Karyawan ~~~\n")
    print("1. Report Semua Data Training Karyawan")
    print("2. Mencari Data Training Karyawan Tertentu")
    print("3. Kembali Ke Menu Utama")
    return input("Silahkan Pilih Sub Menu Report Data [1-3]: ")

def view_submenucreate():
    print("\n~~~ Menambah Data Training Karyawan ~~~\n")
    print("1. Tambah Data Training Karyawan")
    print("2. Kembali Ke Menu Utama")
    return input("Silahkan Pilih Sub Menu Create Data [1-2]: ")

def view_submenuupdate():
    print("\n~~~ Mengubah Data Training Karyawan ~~~\n")
    print("1. Ubah Data Training Karyawan")
    print("2. Kembali Ke Menu Utama")
    return input("Silahkan Pilih Sub Menu Update Data [1-2]: ")

def view_submenudelete():
    print("\n~~~ Menghapus Data Training Karyawan ~~~\n")
    print("1. Hapus Data Training Karyawan")
    print("2. Kembali Ke Menu Utama")
    return input("Silahkan Pilih Sub Menu Hapus Data [1-2]: ")


# --- READ ---

def display_table(rows):
    #"""Menampilkan hasil query dalam format tabel."""
    if not rows:
        print("***Tidak Ada Data Training Karyawan***")
        return

    print("\nDaftar Data Training Karyawan")
    print("=" * 175)
    print(f'{"NIP":<7} {"Nama":<10} {"Jabatan":<30} {"Department":<28} {"Training":<35} '
          f'{"Kategori":<18} {"Provider":<25} {"Tanggal":<12} {"Valid":<6} {"Status":<10}')
    print("=" * 175)
    for row in rows:
        emp_id, emp_name, job_title, dept_name, training_name, training_cat, \
            training_provider, training_date, training_valid, training_status = row
        provider = training_provider if training_provider else "-"
        print(f"{emp_id:<7} {emp_name:<10} {job_title:<30} {dept_name:<28} {training_name:<35} "
              f"{training_cat:<18} {provider:<25} {str(training_date):<12} {str(training_valid):<6} {training_status:<10}")

def read_all_training():
    #"""Menampilkan semua data training karyawan aktif dari database."""
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        query = """
            SELECT
                e.emp_id,
                e.emp_name,
                e.job_title,
                e.dept_name,
                t.training_name,
                t.training_cat,
                t.training_provider,
                h.training_date,
                t.training_valid,
                h.training_status
            FROM training_history_data h
            JOIN employee_data e ON h.emp_id = e.emp_id
            JOIN training_data t ON h.training_id = t.training_id
            ORDER BY e.emp_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        display_table(rows)
    except Error as e:
        print(f"[ERROR] Gagal membaca data: {e}")
    finally:
        cursor.close()
        conn.close()

def search_training(search_NIP):
    #"""Mencari data training berdasarkan NIP karyawan."""
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        query = """
            SELECT
                e.emp_id,
                e.emp_name,
                e.job_title,
                e.dept_name,
                t.training_name,
                t.training_cat,
                t.training_provider,
                h.training_date,
                t.training_valid,
                h.training_status
            FROM training_history_data h
            JOIN employee_data e ON h.emp_id = e.emp_id
            JOIN training_data t ON h.training_id = t.training_id
            WHERE e.emp_id = %s
        """
        cursor.execute(query, (search_NIP,))
        rows = cursor.fetchall()
        display_table(rows)
    except Error as e:
        print(f"[ERROR] Gagal mencari data: {e}")
    finally:
        cursor.close()
        conn.close()


# --- CREATE ---

def cek_training(tr_history_id):
    #"""Cek apakah tr_history_id sudah ada di database."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT tr_history_id FROM training_history_data WHERE tr_history_id = %s", (tr_history_id,))
        result = cursor.fetchone()
        return result is not None
    except Error as e:
        print(f"[ERROR] Gagal cek data: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def cek_emp_exists(emp_id):
    #"""Cek apakah emp_id ada di tabel employee_data."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT emp_id FROM employee_data WHERE emp_id = %s", (emp_id,))
        return cursor.fetchone() is not None
    except Error as e:
        print(f"[ERROR]: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def cek_training_exists(training_id):
    #"""Cek apakah training_id ada di tabel training_data."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT training_id FROM training_data WHERE training_id = %s", (training_id,))
        return cursor.fetchone() is not None
    except Error as e:
        print(f"[ERROR]: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def add_training(tr_history_id, emp_id, training_id, training_date, training_status):
    #"""Menambah data training history karyawan ke database."""
    while True:
        confirm = input("Apakah Data akan disimpan? (Y/N): ").lower()
        if confirm == "y":
            conn = get_connection()
            if not conn:
                return
            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO training_history_data
                        (tr_history_id, emp_id, training_id, training_date, training_status)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (tr_history_id, emp_id, training_id, training_date, training_status))
                conn.commit()
                print("Data Tersimpan")
            except Error as e:
                print(f"[ERROR] Gagal menyimpan data: {e}")
            finally:
                cursor.close()
                conn.close()
            return
        elif confirm == "n":
            print("Data Tidak Ditambahkan")
            return
        else:
            print("Pilihan Salah, Masukkan Y/N")


# --- UPDATE ---

UPDATABLE_FIELDS = {
    "training_date": "training_date",
    "training_status": "training_status"
}

def update_training(search_NIP):
    #"""Mengubah data training history karyawan berdasarkan NIP."""
    # Tampilkan data yang ada dulu
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT tr_history_id FROM training_history_data WHERE emp_id = %s", (search_NIP,)
        )
        records = cursor.fetchall()
    except Error as e:
        print(f"[ERROR]: {e}")
        return
    finally:
        cursor.close()
        conn.close()

    if not records:
        print("***Tidak Ada Data Training Karyawan untuk NIP tersebut***")
        return

    # Jika lebih dari 1 record, minta pilih tr_history_id
    if len(records) == 1:
        tr_history_id = records[0][0]
    else:
        print("Ditemukan beberapa record untuk karyawan ini:")
        for r in records:
            print(f"  - TR History ID: {r[0]}")
        try:
            tr_history_id = int(input("Masukkan TR History ID yang ingin diubah: "))
        except ValueError:
            print("Input tidak valid.")
            return

    while True:
        confirm = input("Tekan Y jika akan mengupdate data dan N untuk membatalkan (Y/N): ").lower()
        if confirm == "y":
            print("Kolom yang dapat diupdate: training_date, training_status")
            updated_field = input("Masukkan Nama Kolom yang Diupdate: ").strip()
            if updated_field not in UPDATABLE_FIELDS:
                print("!! Nama Kolom Salah atau Tidak Dapat Diupdate")
                return
            updated_value = input("Masukkan Nilai Baru: ").strip()
            while True:
                save_value = input("Apakah Data akan Diupdate? (Y/N): ").lower()
                if save_value == "y":
                    conn = get_connection()
                    if not conn:
                        return
                    try:
                        cursor = conn.cursor()
                        query = f"UPDATE training_history_data SET {updated_field} = %s WHERE tr_history_id = %s"
                        cursor.execute(query, (updated_value, tr_history_id))
                        conn.commit()
                        if cursor.rowcount > 0:
                            print("Data Terupdate")
                        else:
                            print("Data tidak ditemukan atau tidak ada perubahan.")
                    except Error as e:
                        print(f"[ERROR] Gagal mengupdate data: {e}")
                    finally:
                        cursor.close()
                        conn.close()
                    return
                elif save_value == "n":
                    print("Data Tidak Diupdate")
                    return
                else:
                    print("Pilihan Salah, Masukkan Y/N")
        elif confirm == "n":
            print("Data Tidak Diupdate")
            return
        else:
            print("Pilihan Salah, Masukkan Y/N")


# --- DELETE ---

def delete_training(search_NIP):
    #"""Menghapus data training history karyawan berdasarkan NIP."""
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT tr_history_id FROM training_history_data WHERE emp_id = %s", (search_NIP,)
        )
        records = cursor.fetchall()
    except Error as e:
        print(f"[ERROR]: {e}")
        return
    finally:
        cursor.close()
        conn.close()

    if not records:
        print("***Tidak Ada Data Training Karyawan untuk NIP tersebut***")
        return

    if len(records) == 1:
        tr_history_id = records[0][0]
    else:
        print("Ditemukan beberapa record untuk karyawan ini:")
        for r in records:
            print(f"  - TR History ID: {r[0]}")
        try:
            tr_history_id = int(input("Masukkan TR History ID yang ingin dihapus: "))
        except ValueError:
            print("Input tidak valid.")
            return

    while True:
        confirm = input("Apakah Data akan Dihapus? (Y/N): ").lower()
        if confirm == "y":
            conn = get_connection()
            if not conn:
                return
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM training_history_data WHERE tr_history_id = %s", (tr_history_id,)
                )
                conn.commit()
                if cursor.rowcount > 0:
                    print("Data Terhapus")
                else:
                    print("Data tidak ditemukan.")
            except Error as e:
                print(f"[ERROR] Gagal menghapus data: {e}")
            finally:
                cursor.close()
                conn.close()
            return
        elif confirm == "n":
            print("Data Tidak Terhapus")
            return
        else:
            print("Pilihan Salah, Masukkan Y/N")


# /===== Main Program =====/

running = True
while running:
    input_mainmenu = main_menu()

    if input_mainmenu == "1":
        submenu_read = True
        while submenu_read:
            input_sub_menuread = view_submenuread()
            if input_sub_menuread == "1":
                read_all_training()
            elif input_sub_menuread == "2":
                search_NIP = input("Masukkan NIP Karyawan: ")
                print(f"Data Training Karyawan dengan NIP: {search_NIP}")
                search_training(search_NIP)
            elif input_sub_menuread == "3":
                submenu_read = False
            else:
                print("***Pilihan yang Anda Masukkan Salah***")

    elif input_mainmenu == "2":
        submenu_create = True
        while submenu_create:
            input_sub_menucreate = view_submenucreate()
            if input_sub_menucreate == "1":
                try:
                    tr_history_id = int(input("Masukkan TR History ID (angka unik): "))
                except ValueError:
                    print("TR History ID harus berupa angka.")
                    continue
                if cek_training(tr_history_id):
                    print("Data Training History dengan ID tersebut sudah ada.")
                    continue
                emp_id = input("Masukkan NIP Karyawan: ")
                if not cek_emp_exists(emp_id):
                    print("!! NIP Karyawan tidak ditemukan di database.")
                    continue
                try:
                    training_id = int(input("Masukkan Training ID: "))
                except ValueError:
                    print("Training ID harus berupa angka.")
                    continue
                if not cek_training_exists(training_id):
                    print("!! Training ID tidak ditemukan di database.")
                    continue
                training_date = input("Masukkan Tanggal Training (YYYY-MM-DD): ")
                training_status = input("Masukkan Status Training (Aktif/Expired): ")
                add_training(tr_history_id, emp_id, training_id, training_date, training_status)
            elif input_sub_menucreate == "2":
                submenu_create = False
            else:
                print("***Pilihan yang Anda Masukkan Salah***")

    elif input_mainmenu == "3":
        submenu_update = True
        while submenu_update:
            input_sub_menuupdate = view_submenuupdate()
            if input_sub_menuupdate == "1":
                search_NIP = input("Masukkan NIP Karyawan: ")
                search_training(search_NIP)
                update_training(search_NIP)
            elif input_sub_menuupdate == "2":
                submenu_update = False
            else:
                print("***Pilihan yang Anda Masukkan Salah***")

    elif input_mainmenu == "4":
        submenu_delete = True
        while submenu_delete:
            input_sub_menudelete = view_submenudelete()
            if input_sub_menudelete == "1":
                search_NIP = input("Masukkan NIP Karyawan: ")
                search_training(search_NIP)
                delete_training(search_NIP)
            elif input_sub_menudelete == "2":
                submenu_delete = False
            else:
                print("***Pilihan yang Anda Masukkan Salah***")

    elif input_mainmenu == "5":
        print("Terima Kasih Sudah Menggunakan Aplikasi")
        running = False

    else:
        print("***Pilihan yang Anda Masukkan Salah***")
