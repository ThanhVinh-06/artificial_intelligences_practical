# -*- coding: utf-8 -*-
"""Tri tue nhan tao - Thuc hanh Buoi 4: Bieu dien tri thuc va suy dien (10 bai)."""
import sys, itertools
from itertools import combinations, count
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sympy import symbols, Implies, Equivalent, And, Or, Not
from sympy.logic.boolalg import to_cnf

sys.stdout.reconfigure(encoding="utf-8")
imp = lambda a, b: (not a) or b
iff = lambda a, b: a == b


def tieu_de(s):
    print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)


# ---------------------------------------------------------------- Bai 1
def bai1():
    tieu_de("BAI 1: Bang chan tri va phan loai")

    def bang_chan_tri(bien, f):
        hang = []
        for vals in itertools.product([False, True], repeat=len(bien)):
            env = dict(zip(bien, vals))
            hang.append(list(vals) + [f(env)])
        return pd.DataFrame(hang, columns=bien + ['KQ'])

    def phan_loai(bien, f):
        kq = bang_chan_tri(bien, f)['KQ']
        if kq.all():
            return 'hang dung'
        if not kq.any():
            return 'mau thuan'
        return 'thoa duoc'

    f1 = lambda e: imp(imp(e['P'], e['Q']) and imp(e['Q'], e['R']), imp(e['P'], e['R']))
    print(bang_chan_tri(['P', 'Q', 'R'], f1))
    assert phan_loai(['P', 'Q', 'R'], f1) == 'hang dung'
    f2 = lambda e: (e['P'] or e['Q']) and (not e['P']) and (not e['Q'])
    f3 = lambda e: imp(e['P'], e['Q']) and imp(e['Q'], not e['P'])
    f4 = lambda e: iff(e['P'], e['Q'] and not e['P'])
    for ten, f, b in [('(a)', f1, 'PQR'), ('(b)', f2, 'PQ'), ('(c)', f3, 'PQ'), ('(d)', f4, 'PQ')]:
        print(ten, phan_loai(list(b), f))
    print("Giai thich: (c) thoa duoc: chi dung khi P=False (tuong duong ~P). "
          "(d) thoa duoc: P=T thi Q&~P=F nen T<->F sai; P=F thi F<->F dung => chi dung khi P=False.")


# ---------------------------------------------------------------- Bai 2
def cac_mo_hinh(bien):
    for vals in itertools.product([False, True], repeat=len(bien)):
        yield dict(zip(bien, vals))


def tuong_duong(bien, f, g):
    return all(f(m) == g(m) for m in cac_mo_hinh(bien))


def he_qua(bien, KB, alpha):
    return all(alpha(m) for m in cac_mo_hinh(bien) if KB(m))


def bai2():
    tieu_de("BAI 2: Tuong duong va he qua")
    print("De Morgan:", tuong_duong(['P', 'Q'], lambda e: not (e['P'] and e['Q']), lambda e: (not e['P']) or (not e['Q'])))
    print("Phan dao:", tuong_duong(['P', 'Q'], lambda e: imp(e['P'], e['Q']), lambda e: imp(not e['Q'], not e['P'])))
    print("P->Q va Q->P:", tuong_duong(['P', 'Q'], lambda e: imp(e['P'], e['Q']), lambda e: imp(e['Q'], e['P'])))
    KB = lambda e: imp(e['P'], e['Q']) and imp(e['Q'], e['R']) and e['P']
    print("KB |= R ?", he_qua(['P', 'Q', 'R'], KB, lambda e: e['R']))
    phat_bieu_A = lambda e: e['A'] == ((not e['A']) and (not e['B']))
    ms = [m for m in cac_mo_hinh(['A', 'B']) if phat_bieu_A(m)]
    print("Mo hinh thoa:", ms)
    for m in ms:
        print("Ket luan: A la", "hiep si" if m['A'] else "ke noi doi", "; B la", "hiep si" if m['B'] else "ke noi doi")


# ---------------------------------------------------------------- Bai 3
P, Q, R = symbols('P Q R')


def literal_str(l):
    return '~' + str(l.args[0]) if isinstance(l, Not) else str(l)


def to_clauses(cnf):
    if isinstance(cnf, And):
        return [frozenset(literal_str(l) for l in (c.args if isinstance(c, Or) else [c])) for c in cnf.args]
    if isinstance(cnf, Or):
        return [frozenset(literal_str(l) for l in cnf.args)]
    return [frozenset([literal_str(cnf)])]


def khu_keo_theo(e):
    if isinstance(e, Implies):
        a, b = khu_keo_theo(e.args[0]), khu_keo_theo(e.args[1])
        return Or(Not(a), b)
    if isinstance(e, Equivalent):
        a, b = khu_keo_theo(e.args[0]), khu_keo_theo(e.args[1])
        return And(Or(Not(a), b), Or(Not(b), a))
    if e.args:
        return e.func(*[khu_keo_theo(a) for a in e.args])
    return e


def bai3():
    tieu_de("BAI 3: CNF")
    for ct in [Equivalent(P, Or(Q, R)), Implies(And(P, Q), R)]:
        c = to_cnf(ct, simplify=True)
        print(ct, "=>", c)
        print(to_clauses(c))
        mine = khu_keo_theo(ct)
        print("  khu_keo_theo:", mine, "| to_cnf:", to_cnf(mine, simplify=True),
              "| trung khop:", to_cnf(mine, simplify=True) == c)


# ---------------------------------------------------------------- Bai 4
def phu_dinh(l):
    return l[1:] if l.startswith('~') else '~' + l


def hop_giai(c1, c2):
    kq = []
    for l in c1:
        if phu_dinh(l) in c2:
            r = (c1 - {l}) | (c2 - {phu_dinh(l)})
            if any(phu_dinh(x) in r for x in r):
                continue
            kq.append(frozenset(r))
    return kq


def fmt(c):
    return "{" + ", ".join(sorted(c)) + "}" if c else "[]"


def pl_resolution(kb, alpha, in_buoc=True):
    clauses = set(kb) | {frozenset([phu_dinh(alpha)])}
    while True:
        moi = set()
        for ci, cj in combinations(list(clauses), 2):
            rs = hop_giai(ci, cj)
            for r in rs:
                if in_buoc and r not in clauses:
                    print(f"   {fmt(ci)} + {fmt(cj)} -> {fmt(r)}")
                if not r:
                    return True
            moi |= set(rs)
        if moi <= clauses:
            return False
        clauses |= moi


def bai4():
    tieu_de("BAI 4: Hop giai menh de")
    KB = [frozenset({'~P', 'Q'}), frozenset({'~Q', 'R'}), frozenset({'P'})]
    print("KB |= R:", pl_resolution(KB, 'R'))
    print("KB |= ~R:", pl_resolution(KB, '~R'))


# ---------------------------------------------------------------- Bai 5
def bai5():
    tieu_de("BAI 5: Logic vi tu tren mien huu han")
    mien = ['An', 'Binh', 'Cuong', 'Dung']
    SinhVien = {'An', 'Binh', 'Cuong'}
    ChamChi = {'An', 'Binh'}
    Quen = {('An', 'Binh'), ('Binh', 'An'), ('Cuong', 'An'), ('Dung', 'Binh'), ('An', 'Cuong'), ('Binh', 'Cuong')}
    forall = lambda D, p: all(p(x) for x in D)
    exists = lambda D, p: any(p(x) for x in D)
    print("(a)", forall(mien, lambda x: imp(x in SinhVien, x in ChamChi)))
    print("   phan vi du:", [x for x in mien if x in SinhVien and x not in ChamChi])
    print("(b)", exists(mien, lambda x: x in SinhVien and x not in ChamChi))
    print("(c)", forall(mien, lambda x: exists(mien, lambda y: (x, y) in Quen)))
    print("(d)", exists(mien, lambda y: forall(mien, lambda x: (x, y) in Quen)))
    print("   (y nao ma ai cung quen: khong ai vi x=y khong co (y,y); neu bo qua x=y:",
          [y for y in mien if all((x, y) in Quen for x in mien if x != y)], ")")
    Ps = [lambda x: x in SinhVien, lambda x: x in ChamChi, lambda x: True]
    for k, p in enumerate(Ps, 1):
        print(f"(e) P{k}:", (not forall(mien, p)) == exists(mien, lambda x: not p(x)))


# ---------------------------------------------------------------- Bai 6
def is_var(t):
    return isinstance(t, str) and t.startswith('?')


def subst(theta, t):
    if is_var(t):
        return subst(theta, theta[t]) if t in theta else t
    if isinstance(t, tuple):
        return tuple(subst(theta, a) for a in t)
    return t


def occur_check(v, t, theta):
    t = subst(theta, t)
    if is_var(t):
        return v == t
    if isinstance(t, tuple):
        return any(occur_check(v, a, theta) for a in t)
    return False


def unify_var(v, t, theta):
    if v in theta:
        return unify(theta[v], t, theta)
    if is_var(t) and t in theta:
        return unify(v, theta[t], theta)
    if occur_check(v, t, theta):
        return None
    return {**theta, v: t}


def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if x == y:
        return theta
    if is_var(x):
        return unify_var(x, y, theta)
    if is_var(y):
        return unify_var(y, x, theta)
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            theta = unify(a, b, theta)
            if theta is None:
                return None
        return theta
    return None


def mgu(x, y):
    t = unify(x, y)
    return None if t is None else {k: subst(t, v) for k, v in t.items()}


def bai6():
    tieu_de("BAI 6: Unification")
    print(mgu(('Knows', 'John', '?x'), ('Knows', '?y', 'Mary')))
    print(mgu(('P', '?x', '?x'), ('P', 'A', 'B')), "(None)")
    print(mgu('?x', ('f', '?x')), "(None - occur check)")
    print(mgu(('Knows', 'John', '?x'), ('Knows', '?y', ('Mother', '?y'))))
    print("Test rieng:")
    print(" 1.", mgu(('Loves', '?x', ('Wife', '?x')), ('Loves', 'Tom', '?z')), "thanh cong")
    print(" 2.", mgu(('P', 'A'), ('P', 'B')), "that bai: hai hang khac nhau")
    print(" 3.", mgu(('P', '?x', 'A'), ('P', 'B')), "that bai: khac so doi so")


# ---------------------------------------------------------------- Bai 7
_dem = count()


def doi_ten(clause):
    k = next(_dem)

    def r(t):
        if is_var(t):
            return f"{t}_{k}"
        if isinstance(t, tuple):
            return tuple(r(a) for a in t)
        return t
    return [(s, r(a)) for s, a in clause]


def don_gian(clause):
    ra = []
    for l in clause:
        if l not in ra:
            ra.append(l)
    return ra


def hop_giai_fol(c1, c2):
    c1, c2 = doi_ten(c1), doi_ten(c2)
    kq = []
    for i, (s1, a1) in enumerate(c1):
        for j, (s2, a2) in enumerate(c2):
            if s1 != s2:
                theta = unify(a1, a2)
                if theta is not None:
                    moi = [(s, subst(theta, a)) for s, a in c1[:i] + c1[i + 1:] + c2[:j] + c2[j + 1:]]
                    kq.append(don_gian(moi))
    return kq


def chuan_hoa(c):
    """Dua bien ve dang ?v0, ?v1... de nhan dien clause trung nhau."""
    m = {}

    def r(t):
        if is_var(t):
            return m.setdefault(t, f"?v{len(m)}")
        if isinstance(t, tuple):
            return tuple(r(a) for a in t)
        return t
    return frozenset((s, r(a)) for s, a in c)


def chung_minh_fol(kb, truy_van, gioi_han=3000, in_buoc=True):
    clauses = [list(c) for c in kb] + [[(False, truy_van)]]
    biet = {chuan_hoa(c) for c in clauses}
    dung = 0
    # unit preference: duyet cap co tong do dai nho truoc (BFS theo muc do dai)
    i = 0
    while i < len(clauses):
        for j in range(i):
            for rs in sorted(hop_giai_fol(clauses[j], clauses[i]), key=len):
                dung += 1
                if dung > gioi_han:
                    return False, dung
                if not rs:
                    if in_buoc:
                        print(f"   ({j+1}, {i+1}) -> []")
                    return True, dung
                k = chuan_hoa(rs)
                if k not in biet:
                    biet.add(k)
                    clauses.append(rs)
                    if in_buoc:
                        print(f"   ({j+1}, {i+1}) -> {len(clauses)}: {rs}")
        i += 1
    return False, dung


def bai7():
    tieu_de("BAI 7: Hop giai Robinson cho FOL")
    KB_a = [[(False, ('Cho', '?x')), (True, ('DongVat', '?x'))],
            [(False, ('DongVat', '?x')), (True, ('Chet', '?x'))],
            [(True, ('Cho', 'Rex'))]]
    print("(a)", chung_minh_fol(KB_a, ('Chet', 'Rex')))
    KB_b = [[(False, ('BoMe', '?x', '?y')), (False, ('Nam', '?x')), (True, ('Cha', '?x', '?y'))],
            [(True, ('BoMe', 'An', 'Binh'))], [(True, ('Nam', 'An'))]]
    print("(b)", chung_minh_fol(KB_b, ('Cha', 'An', 'Binh')))
    KB_c = [
        [(True, ('Nguoi', 'Marcus'))],
        [(True, ('Pompeii', 'Marcus'))],
        [(False, ('Pompeii', '?x')), (True, ('LaMa', '?x'))],
        [(True, ('CaiTri', 'Caesar'))],
        [(False, ('LaMa', '?x')), (True, ('TrungThanh', '?x', 'Caesar')), (True, ('CamGhet', '?x', 'Caesar'))],
        [(True, ('TrungThanh', '?x', ('f', '?x')))],
        [(False, ('Nguoi', '?x')), (False, ('CaiTri', '?y')), (False, ('AmSat', '?x', '?y')), (False, ('TrungThanh', '?x', '?y'))],
        [(True, ('AmSat', 'Marcus', 'Caesar'))],
    ]
    print("(c)", chung_minh_fol(KB_c, ('CamGhet', 'Marcus', 'Caesar')))
    print("(sai) khong suy ra:", chung_minh_fol(KB_a, ('Chet', 'Tom'), in_buoc=False))


# ---------------------------------------------------------------- Bai 8
def bai8():
    tieu_de("BAI 8: Mang ngu nghia")
    G = nx.DiGraph()
    quan_he = [('Chim', 'DongVat', 'is_a'), ('Ca', 'DongVat', 'is_a'),
               ('ChimCanhCut', 'Chim', 'is_a'), ('Chim_Se', 'Chim', 'is_a'),
               ('Tweety', 'Chim_Se', 'is_a'), ('Pingu', 'ChimCanhCut', 'is_a')]
    for a, b, r in quan_he:
        G.add_edge(a, b, rel=r)
    thuoc_tinh = {'DongVat': {'di_chuyen': True, 'bay_duoc': False},
                  'Chim': {'co_canh': True, 'bay_duoc': True},
                  'Ca': {'boi_duoc': True},
                  'ChimCanhCut': {'bay_duoc': False, 'song_o': 'Nam Cuc'}}

    def cha(nut):
        return [v for _, v, d in G.out_edges(nut, data=True) if d['rel'] == 'is_a']

    def tim_thuoc_tinh(nut, khoa):
        if khoa in thuoc_tinh.get(nut, {}):
            return thuoc_tinh[nut][khoa]
        for c in cha(nut):
            v = tim_thuoc_tinh(c, khoa)
            if v is not None:
                return v
        return None

    def tat_ca_thuoc_tinh(nut):
        kq = {}
        for c in cha(nut):
            for k, v in tat_ca_thuoc_tinh(c).items():
                kq.setdefault(k, v)
        kq.update(thuoc_tinh.get(nut, {}))
        return kq

    def la_loai(a, b):
        return a != b and nx.has_path(G, a, b)

    print(tim_thuoc_tinh('Tweety', 'bay_duoc'))
    print(tim_thuoc_tinh('Pingu', 'bay_duoc'))
    print(tat_ca_thuoc_tinh('Pingu'))
    print(la_loai('Pingu', 'DongVat'), la_loai('Ca', 'Chim'))
    print("Tweety bay duoc?", tim_thuoc_tinh('Tweety', 'bay_duoc'), "| Pingu bay duoc?", tim_thuoc_tinh('Pingu', 'bay_duoc'))
    pos = nx.spring_layout(G, seed=7)
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_color='#cfe8ff', node_size=2200, font_size=9, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'rel'), font_size=8)
    plt.savefig("mang_ngu_nghia.png", dpi=100)
    plt.close()
    print("Da luu mang_ngu_nghia.png")


# ---------------------------------------------------------------- Bai 9
RULES9 = [
    ('R1', {'co_long'}, 'la_thu'),
    ('R2', {'cho_sua'}, 'la_thu'),
    ('R3', {'co_long_vu'}, 'la_chim'),
    ('R4', {'biet_bay', 'de_trung'}, 'la_chim'),
    ('R5', {'la_thu', 'an_thit'}, 'la_thu_an_thit'),
    ('R6', {'la_thu_an_thit', 'mau_vang_nau', 'co_van_den'}, 'la_ho'),
    ('R7', {'la_thu_an_thit', 'mau_vang_nau', 'co_dom_den'}, 'la_bao'),
    ('R8', {'la_chim', 'khong_biet_bay', 'boi_gioi'}, 'la_chim_canh_cut'),
    # luat moi (c)
    ('R9', {'co_vay', 'boi_duoi_nuoc'}, 'la_ca'),
    ('R10', {'khong_chan', 'bo_sat', 'co_vay_sung'}, 'la_ran'),
]


def suy_dien_tien(rules, facts, chien_luoc="thu_tu"):
    facts = set(facts)
    vet = []
    vong = 0
    thay_doi = True
    while thay_doi:
        thay_doi = False
        vong += 1
        ds = [r for r in rules if r[1] <= facts and r[2] not in facts]
        if not ds:
            break
        if chien_luoc == "specificity":
            ds = [max(ds, key=lambda r: len(r[1]))]
        else:
            ds = [ds[0]] if chien_luoc == "tung_luat" else ds
        for ten, dk, kl in ds:
            if kl not in facts:
                facts.add(kl)
                vet.append((ten, kl))
                thay_doi = True
    return facts, vet, vong


def bai9():
    tieu_de("BAI 9: Suy dien tien")
    tests = [{'co_long', 'an_thit', 'mau_vang_nau', 'co_van_den'},
             {'biet_bay', 'de_trung'},
             {'co_long_vu', 'khong_biet_bay', 'boi_gioi'},
             {'co_vay', 'boi_duoi_nuoc'},
             {'khong_chan', 'bo_sat', 'co_vay_sung'}]
    for f in tests:
        kq, vet, _ = suy_dien_tien(RULES9, f)
        print(sorted(f), "=>", sorted(kq - f))
        for ten, kl in vet:
            print(f"   {ten}: => {kl}")
    assert 'la_ho' in suy_dien_tien(RULES9, tests[0])[0]
    print("So sanh vong lap (bo su kien 1):")
    for cl in ["thu_tu", "tung_luat", "specificity"]:
        _, vet, vong = suy_dien_tien(RULES9, tests[0], cl)
        print(f"   {cl}: {vong} vong, {len(vet)} luat bi bat")


# ---------------------------------------------------------------- Bai 10
def bai10():
    tieu_de("BAI 10: Suy dien lui - he chuyen gia mini")
    RULES = [
        ('R1', ['khong_den_nguon', 'quat_dung'], 'hong_nguon'),
        ('R2', ['bip_dai_lap_lai', 'khong_hinh'], 'loi_ram'),
        ('R3', ['den_nguon_sang', 'quat_quay', 'khong_hinh', 'khong_tieng_bip'], 'loi_man_hinh'),
        ('R4', ['co_hinh', 'bao_khong_tim_thay_o_dia'], 'loi_o_cung'),
        ('R5', ['hong_nguon'], 'can_thay_linh_kien'),
        ('R6', ['loi_ram'], 'can_thay_linh_kien'),
        # 2 luat de xuat them
        ('R7', ['den_nguon_sang', 'quat_quay', 'co_hinh', 'chay_cham'], 'day_o_cung'),
        ('R8', ['loi_o_cung'], 'can_thay_linh_kien'),
    ]
    KET_LUAN = {kl for _, _, kl in RULES}
    DUNG_INPUT = False
    TRA_LOI_MAU = {'bip_dai_lap_lai': True, 'khong_hinh': True, 'khong_den_nguon': False,
                   'den_nguon_sang': True, 'quat_quay': True, 'khong_tieng_bip': False,
                   'co_hinh': False, 'bao_khong_tim_thay_o_dia': False, 'quat_dung': False}
    da_biet = {}
    CAY_HOW = {}

    def hoi(su_kien, luat):
        if su_kien in da_biet:
            return da_biet[su_kien]
        print(f"   [WHY] Dang can xac dinh '{su_kien}' de kiem tra luat {luat}.")
        if DUNG_INPUT:
            tl = input(f"   '{su_kien}'? (co/khong): ").strip().lower() == 'co'
        else:
            tl = TRA_LOI_MAU.get(su_kien, False)
        da_biet[su_kien] = tl
        return tl

    def chung_minh(mt, luat='(truy van)'):
        if mt not in KET_LUAN:
            return hoi(mt, luat)
        for ten, dk, kl in RULES:
            if kl == mt and all(chung_minh(d, ten) for d in dk):
                CAY_HOW[mt] = (ten, dk)
                return True
        return False

    def in_how(mt, thut=0):
        if mt in CAY_HOW:
            ten, dk = CAY_HOW[mt]
            print("   " + "  " * thut + f"{mt} <= {ten}: {', '.join(dk)}")
            for d in dk:
                in_how(d, thut + 1)
        else:
            print("   " + "  " * thut + f"{mt} (su kien: {da_biet.get(mt)})")

    for mt in ['hong_nguon', 'loi_ram', 'loi_man_hinh', 'loi_o_cung', 'can_thay_linh_kien']:
        kq = chung_minh(mt)
        print(mt, "=>", kq)
        if kq:
            in_how(mt)
    print("Xac nhan:", [m for m in ['hong_nguon', 'loi_ram', 'loi_man_hinh', 'loi_o_cung'] if chung_minh(m)])
    print("Giai thich: 'khong_hinh' da luu trong da_biet nen lan sau hoi() tra ve ngay, khong hoi lai.")


if __name__ == "__main__":
    for b in [bai1, bai2, bai3, bai4, bai5, bai6, bai7, bai8, bai9, bai10]:
        b()

