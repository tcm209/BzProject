! function (t, e) {
    "object" == typeof exports && "object" == typeof module ? module.exports = e() : "function" == typeof define && define.amd ? define("Fangcloud", [], e) : "object" == typeof exports ? exports.Fangcloud = e() : t.Fangcloud = e()
}(window, function () {
    return function (t) {
        var e = {};

        function n(r) {
            if (e[r]) return e[r].exports;
            var o = e[r] = {
                i: r,
                l: !1,
                exports: {}
            };
            return t[r].call(o.exports, o, o.exports, n), o.l = !0, o.exports
        }
        return n.m = t, n.c = e, n.d = function (t, e, r) {
            n.o(t, e) || Object.defineProperty(t, e, {
                enumerable: !0,
                get: r
            })
        }, n.r = function (t) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
                value: "Module"
            }), Object.defineProperty(t, "__esModule", {
                value: !0
            })
        }, n.t = function (t, e) {
            if (1 & e && (t = n(t)), 8 & e) return t;
            if (4 & e && "object" == typeof t && t && t.__esModule) return t;
            var r = Object.create(null);
            if (n.r(r), Object.defineProperty(r, "default", {
                enumerable: !0,
                value: t
            }), 2 & e && "string" != typeof t)
                for (var o in t) n.d(r, o, function (e) {
                    return t[e]
                }.bind(null, o));
            return r
        }, n.n = function (t) {
            var e = t && t.__esModule ? function () {
                return t.default
            } : function () {
                return t
            };
            return n.d(e, "a", e), e
        }, n.o = function (t, e) {
            return Object.prototype.hasOwnProperty.call(t, e)
        }, n.p = "", n(n.s = 69)
    }([
        function (t, e) {
            var n = t.exports = "undefined" != typeof window && window.Math == Math ? window : "undefined" != typeof self && self.Math == Math ? self : Function("return this")();
            "number" == typeof __g && (__g = n)
        },
        function (t, e, n) {
            var r = n(31)("wks"),
                o = n(19),
                i = n(0).Symbol,
                c = "function" == typeof i;
            (t.exports = function (t) {
                return r[t] || (r[t] = c && i[t] || (c ? i : o)("Symbol." + t))
            }).store = r
        },
        function (t, e, n) {
            var r = n(14),
                o = n(16);
            t.exports = n(6) ? function (t, e, n) {
                return r.f(t, e, o(1, n))
            } : function (t, e, n) {
                return t[e] = n, t
            }
        },
        function (t, e, n) {
            var r = n(57);
            t.exports = function (t) {
                for (var e = 1; e < arguments.length; e++) {
                    var n = null != arguments[e] ? arguments[e] : {},
                        o = Object.keys(n);
                    "function" == typeof Object.getOwnPropertySymbols && (o = o.concat(Object.getOwnPropertySymbols(n).filter(function (t) {
                        return Object.getOwnPropertyDescriptor(n, t).enumerable
                    }))), o.forEach(function (e) {
                        r(t, e, n[e])
                    })
                }
                return t
            }
        },
        function (t, e) {
            var n = {}.hasOwnProperty;
            t.exports = function (t, e) {
                return n.call(t, e)
            }
        },
        function (t, e) {
            t.exports = function (t) {
                return "object" == typeof t ? null !== t : "function" == typeof t
            }
        },
        function (t, e, n) {
            t.exports = !n(7)(function () {
                return 7 != Object.defineProperty({}, "a", {
                    get: function () {
                        return 7
                    }
                }).a
            })
        },
        function (t, e) {
            t.exports = function (t) {
                try {
                    return !!t()
                } catch (t) {
                    return !0
                }
            }
        },
        function (t, e) {
            t.exports = function (t) {
                if (void 0 == t) throw TypeError("Can't call method on  " + t);
                return t
            }
        },
        function (t, e, n) {
            var r = n(0),
                o = n(13),
                i = n(2),
                c = n(10),
                u = n(24),
                s = function (t, e, n) {
                    var a, f, l, p, d = t & s.F,
                        h = t & s.G,
                        v = t & s.S,
                        y = t & s.P,
                        m = t & s.B,
                        g = h ? r : v ? r[e] || (r[e] = {}) : (r[e] || {}).prototype,
                        b = h ? o : o[e] || (o[e] = {}),
                        x = b.prototype || (b.prototype = {});
                    for (a in h && (n = e), n) l = ((f = !d && g && void 0 !== g[a]) ? g : n)[a], p = m && f ? u(l, r) : y && "function" == typeof l ? u(Function.call, l) : l, g && c(g, a, l, t & s.U), b[a] != l && i(b, a, p), y && x[a] != l && (x[a] = l)
                };
            r.core = o, s.F = 1, s.G = 2, s.S = 4, s.P = 8, s.B = 16, s.W = 32, s.U = 64, s.R = 128, t.exports = s
        },
        function (t, e, n) {
            var r = n(0),
                o = n(2),
                i = n(4),
                c = n(19)("src"),
                u = Function.toString,
                s = ("" + u).split("toString");
            n(13).inspectSource = function (t) {
                return u.call(t)
            }, (t.exports = function (t, e, n, u) {
                var a = "function" == typeof n;
                a && (i(n, "name") || o(n, "name", e)), t[e] !== n && (a && (i(n, c) || o(n, c, t[e] ? "" + t[e] : s.join(String(e)))), t === r ? t[e] = n : u ? t[e] ? t[e] = n : o(t, e, n) : (delete t[e], o(t, e, n)))
            })(Function.prototype, "toString", function () {
                return "function" == typeof this && this[c] || u.call(this)
            })
        },
        function (t, e, n) {
            var r = n(5);
            t.exports = function (t) {
                if (!r(t)) throw TypeError(t + " is not an object!");
                return t
            }
        },
        function (t, e, n) {
            var r = n(48),
                o = n(8);
            t.exports = function (t) {
                return r(o(t))
            }
        },
        function (t, e) {
            var n = t.exports = {
                version: "2.5.7"
            };
            "number" == typeof __e && (__e = n)
        },
        function (t, e, n) {
            var r = n(11),
                o = n(26),
                i = n(17),
                c = Object.defineProperty;
            e.f = n(6) ? Object.defineProperty : function (t, e, n) {
                if (r(t), e = i(e, !0), r(n), o) try {
                    return c(t, e, n)
                } catch (t) {}
                if ("get" in n || "set" in n) throw TypeError("Accessors not supported!");
                return "value" in n && (t[e] = n.value), t
            }
        },
        function (t, e) {
            var n = {}.toString;
            t.exports = function (t) {
                return n.call(t).slice(8, -1)
            }
        },
        function (t, e) {
            t.exports = function (t, e) {
                return {
                    enumerable: !(1 & t),
                    configurable: !(2 & t),
                    writable: !(4 & t),
                    value: e
                }
            }
        },
        function (t, e, n) {
            var r = n(5);
            t.exports = function (t, e) {
                if (!r(t)) return t;
                var n, o;
                if (e && "function" == typeof (n = t.toString) && !r(o = n.call(t))) return o;
                if ("function" == typeof (n = t.valueOf) && !r(o = n.call(t))) return o;
                if (!e && "function" == typeof (n = t.toString) && !r(o = n.call(t))) return o;
                throw TypeError("Can't convert object to primitive value")
            }
        },
        function (t, e, n) {
            var r = n(31)("keys"),
                o = n(19);
            t.exports = function (t) {
                return r[t] || (r[t] = o(t))
            }
        },
        function (t, e) {
            var n = 0,
                r = Math.random();
            t.exports = function (t) {
                return "Symbol(".concat(void 0 === t ? "" : t, ")_", (++n + r).toString(36))
            }
        },
        function (t, e) {
            t.exports = "constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")
        },
        function (t, e, n) {
            var r = n(28),
                o = n(20);
            t.exports = Object.keys || function (t) {
                return r(t, o)
            }
        },
        function (t, e) {
            t.exports = {}
        },
        function (t, e) {
            t.exports = function (t, e) {
                if (!(t instanceof e)) throw new TypeError("Cannot call a class as a function")
            }
        },
        function (t, e, n) {
            var r = n(46);
            t.exports = function (t, e, n) {
                if (r(t), void 0 === e) return t;
                switch (n) {
                case 1:
                    return function (n) {
                        return t.call(e, n)
                    };
                case 2:
                    return function (n, r) {
                        return t.call(e, n, r)
                    };
                case 3:
                    return function (n, r, o) {
                        return t.call(e, n, r, o)
                    }
                }
                return function () {
                    return t.apply(e, arguments)
                }
            }
        },
        function (t, e, n) {
            var r = n(47),
                o = n(16),
                i = n(12),
                c = n(17),
                u = n(4),
                s = n(26),
                a = Object.getOwnPropertyDescriptor;
            e.f = n(6) ? a : function (t, e) {
                if (t = i(t), e = c(e, !0), s) try {
                    return a(t, e)
                } catch (t) {}
                if (u(t, e)) return o(!r.f.call(t, e), t[e])
            }
        },
        function (t, e, n) {
            t.exports = !n(6) && !n(7)(function () {
                return 7 != Object.defineProperty(n(27)("div"), "a", {
                    get: function () {
                        return 7
                    }
                }).a
            })
        },
        function (t, e, n) {
            var r = n(5),
                o = n(0).document,
                i = r(o) && r(o.createElement);
            t.exports = function (t) {
                return i ? o.createElement(t) : {}
            }
        },
        function (t, e, n) {
            var r = n(4),
                o = n(12),
                i = n(29)(!1),
                c = n(18)("IE_PROTO");
            t.exports = function (t, e) {
                var n, u = o(t),
                    s = 0,
                    a = [];
                for (n in u) n != c && r(u, n) && a.push(n);
                for (; e.length > s;) r(u, n = e[s++]) && (~i(a, n) || a.push(n));
                return a
            }
        },
        function (t, e, n) {
            var r = n(12),
                o = n(50),
                i = n(51);
            t.exports = function (t) {
                return function (e, n, c) {
                    var u, s = r(e),
                        a = o(s.length),
                        f = i(c, a);
                    if (t && n != n) {
                        for (; a > f;)
                            if ((u = s[f++]) != u) return !0
                    } else
                        for (; a > f; f++)
                            if ((t || f in s) && s[f] === n) return t || f || 0; return !t && -1
                }
            }
        },
        function (t, e) {
            var n = Math.ceil,
                r = Math.floor;
            t.exports = function (t) {
                return isNaN(t = +t) ? 0 : (t > 0 ? r : n)(t)
            }
        },
        function (t, e, n) {
            var r = n(13),
                o = n(0),
                i = o["__core-js_shared__"] || (o["__core-js_shared__"] = {});
            (t.exports = function (t, e) {
                return i[t] || (i[t] = void 0 !== e ? e : {})
            })("versions", []).push({
                version: r.version,
                mode: n(32) ? "pure" : "global",
                copyright: "? 2018 Denis Pushkarev (zloirock.ru)"
            })
        },
        function (t, e) {
            t.exports = !1
        },
        function (t, e, n) {
            var r = n(11),
                o = n(54),
                i = n(20),
                c = n(18)("IE_PROTO"),
                u = function () {},
                s = function () {
                    var t, e = n(27)("iframe"),
                        r = i.length;
                    for (e.style.display = "none", n(55).appendChild(e), e.src = "javascript:", (t = e.contentWindow.document).open(), t.write("<script>document.F=Object<\/script>"), t.close(), s = t.F; r--;) delete s.prototype[i[r]];
                    return s()
                };
            t.exports = Object.create || function (t, e) {
                var n;
                return null !== t ? (u.prototype = r(t), n = new u, u.prototype = null, n[c] = t) : n = s(), void 0 === e ? n : o(n, e)
            }
        },
        function (t, e, n) {
            "use strict";
            var r = n(2),
                o = n(10),
                i = n(7),
                c = n(8),
                u = n(1);
            t.exports = function (t, e, n) {
                var s = u(t),
                    a = n(c, s, "" [t]),
                    f = a[0],
                    l = a[1];
                i(function () {
                    var e = {};
                    return e[s] = function () {
                        return 7
                    }, 7 != "" [t](e)
                }) && (o(String.prototype, t, f), r(RegExp.prototype, s, 2 == e ? function (t, e) {
                    return l.call(t, this, e)
                } : function (t) {
                    return l.call(t, this)
                }))
            }
        },
        function (t, e, n) {
            var r = n(5),
                o = n(15),
                i = n(1)("match");
            t.exports = function (t) {
                var e;
                return r(t) && (void 0 !== (e = t[i]) ? !!e : "RegExp" == o(t))
            }
        },
        function (t, e, n) {
            "use strict";
            var r = n(37),
                o = n(60),
                i = n(22),
                c = n(12);
            t.exports = n(61)(Array, "Array", function (t, e) {
                this._t = c(t), this._i = 0, this._k = e
            }, function () {
                var t = this._t,
                    e = this._k,
                    n = this._i++;
                return !t || n >= t.length ? (this._t = void 0, o(1)) : o(0, "keys" == e ? n : "values" == e ? t[n] : [n, t[n]])
            }, "values"), i.Arguments = i.Array, r("keys"), r("values"), r("entries")
        },
        function (t, e, n) {
            var r = n(1)("unscopables"),
                o = Array.prototype;
            void 0 == o[r] && n(2)(o, r, {}), t.exports = function (t) {
                o[r][t] = !0
            }
        },
        function (t, e, n) {
            var r = n(14).f,
                o = n(4),
                i = n(1)("toStringTag");
            t.exports = function (t, e, n) {
                t && !o(t = n ? t : t.prototype, i) && r(t, i, {
                    configurable: !0,
                    value: e
                })
            }
        },
        function (t, e, n) {
            var r = n(8);
            t.exports = function (t) {
                return Object(r(t))
            }
        },
        function (t, e, n) {
            "use strict";
            var r = n(9),
                o = n(29)(!0);
            r(r.P, "Array", {
                includes: function (t) {
                    return o(this, t, arguments.length > 1 ? arguments[1] : void 0)
                }
            }), n(37)("includes")
        },
        function (t, e, n) {
            "use strict";
            var r = n(9),
                o = n(67);
            r(r.P + r.F * n(68)("includes"), "String", {
                includes: function (t) {
                    return !!~o(this, t, "includes").indexOf(t, arguments.length > 1 ? arguments[1] : void 0)
                }
            })
        },
        function (t, e, n) {
            var r = n(59);
            t.exports = function (t, e) {
                if (null == t) return {};
                var n, o, i = r(t, e);
                if (Object.getOwnPropertySymbols) {
                    var c = Object.getOwnPropertySymbols(t);
                    for (o = 0; o < c.length; o++) n = c[o], e.indexOf(n) >= 0 || Object.prototype.propertyIsEnumerable.call(t, n) && (i[n] = t[n])
                }
                return i
            }
        },
        function (t, e, n) {
            "use strict";
            var r = n(0),
                o = n(4),
                i = n(15),
                c = n(44),
                u = n(17),
                s = n(7),
                a = n(49).f,
                f = n(25).f,
                l = n(14).f,
                p = n(52).trim,
                d = r.Number,
                h = d,
                v = d.prototype,
                y = "Number" == i(n(33)(v)),
                m = "trim" in String.prototype,
                g = function (t) {
                    var e = u(t, !1);
                    if ("string" == typeof e && e.length > 2) {
                        var n, r, o, i = (e = m ? e.trim() : p(e, 3)).charCodeAt(0);
                        if (43 === i || 45 === i) {
                            if (88 === (n = e.charCodeAt(2)) || 120 === n) return NaN
                        } else if (48 === i) {
                            switch (e.charCodeAt(1)) {
                            case 66:
                            case 98:
                                r = 2, o = 49;
                                break;
                            case 79:
                            case 111:
                                r = 8, o = 55;
                                break;
                            default:
                                return +e
                            }
                            for (var c, s = e.slice(2), a = 0, f = s.length; a < f; a++)
                                if ((c = s.charCodeAt(a)) < 48 || c > o) return NaN;
                            return parseInt(s, r)
                        }
                    }
                    return +e
                };
            if (!d(" 0o1") || !d("0b1") || d("+0x1")) {
                d = function (t) {
                    var e = arguments.length < 1 ? 0 : t,
                        n = this;
                    return n instanceof d && (y ? s(function () {
                        v.valueOf.call(n)
                    }) : "Number" != i(n)) ? c(new h(g(e)), n, d) : g(e)
                };
                for (var b, x = n(6) ? a(h) : "MAX_VALUE,MIN_VALUE,NaN,NEGATIVE_INFINITY,POSITIVE_INFINITY,EPSILON,isFinite,isInteger,isNaN,isSafeInteger,MAX_SAFE_INTEGER,MIN_SAFE_INTEGER,parseFloat,parseInt,isInteger".split(","), _ = 0; x.length > _; _++) o(h, b = x[_]) && !o(d, b) && l(d, b, f(h, b));
                d.prototype = v, v.constructor = d, n(10)(r, "Number", d)
            }
        },
        function (t, e, n) {
            var r = n(5),
                o = n(45).set;
            t.exports = function (t, e, n) {
                var i, c = e.constructor;
                return c !== n && "function" == typeof c && (i = c.prototype) !== n.prototype && r(i) && o && o(t, i), t
            }
        },
        function (t, e, n) {
            var r = n(5),
                o = n(11),
                i = function (t, e) {
                    if (o(t), !r(e) && null !== e) throw TypeError(e + ": can't set as prototype!")
                };
            t.exports = {
                set: Object.setPrototypeOf || ("__proto__" in {} ? function (t, e, r) {
                    try {
                        (r = n(24)(Function.call, n(25).f(Object.prototype, "__proto__").set, 2))(t, []), e = !(t instanceof Array)
                    } catch (t) {
                        e = !0
                    }
                    return function (t, n) {
                        return i(t, n), e ? t.__proto__ = n : r(t, n), t
                    }
                }({}, !1) : void 0),
                check: i
            }
        },
        function (t, e) {
            t.exports = function (t) {
                if ("function" != typeof t) throw TypeError(t + " is not a function!");
                return t
            }
        },
        function (t, e) {
            e.f = {}.propertyIsEnumerable
        },
        function (t, e, n) {
            var r = n(15);
            t.exports = Object("z").propertyIsEnumerable(0) ? Object : function (t) {
                return "String" == r(t) ? t.split("") : Object(t)
            }
        },
        function (t, e, n) {
            var r = n(28),
                o = n(20).concat("length", "prototype");
            e.f = Object.getOwnPropertyNames || function (t) {
                return r(t, o)
            }
        },
        function (t, e, n) {
            var r = n(30),
                o = Math.min;
            t.exports = function (t) {
                return t > 0 ? o(r(t), 9007199254740991) : 0
            }
        },
        function (t, e, n) {
            var r = n(30),
                o = Math.max,
                i = Math.min;
            t.exports = function (t, e) {
                return (t = r(t)) < 0 ? o(t + e, 0) : i(t, e)
            }
        },
        function (t, e, n) {
            var r = n(9),
                o = n(8),
                i = n(7),
                c = n(53),
                u = "[" + c + "]",
                s = RegExp("^" + u + u + "*"),
                a = RegExp(u + u + "*$"),
                f = function (t, e, n) {
                    var o = {},
                        u = i(function () {
                            return !!c[t]() || "??" != "??" [t]()
                        }),
                        s = o[t] = u ? e(l) : c[t];
                    n && (o[n] = s), r(r.P + r.F * u, "String", o)
                },
                l = f.trim = function (t, e) {
                    return t = String(o(t)), 1 & e && (t = t.replace(s, "")), 2 & e && (t = t.replace(a, "")), t
                };
            t.exports = f
        },
        function (t, e) {
            t.exports = "\t\n\v\f\r ????????????????¡¡\u2028\u2029\ufeff"
        },
        function (t, e, n) {
            var r = n(14),
                o = n(11),
                i = n(21);
            t.exports = n(6) ? Object.defineProperties : function (t, e) {
                o(t);
                for (var n, c = i(e), u = c.length, s = 0; u > s;) r.f(t, n = c[s++], e[n]);
                return t
            }
        },
        function (t, e, n) {
            var r = n(0).document;
            t.exports = r && r.documentElement
        },
        function (t, e, n) {
            n(34)("match", 1, function (t, e, n) {
                return [
                    function (n) {
                        "use strict";
                        var r = t(this),
                            o = void 0 == n ? void 0 : n[e];
                        return void 0 !== o ? o.call(n, r) : new RegExp(n)[e](String(r))
                    },
                    n
                ]
            })
        },
        function (t, e) {
            t.exports = function (t, e, n) {
                return e in t ? Object.defineProperty(t, e, {
                    value: n,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : t[e] = n, t
            }
        },
        function (t, e, n) {
            n(34)("split", 2, function (t, e, r) {
                "use strict";
                var o = n(35),
                    i = r,
                    c = [].push;
                if ("c" == "abbc".split(/(b)*/)[1] || 4 != "test".split(/(?:)/, -1).length || 2 != "ab".split(/(?:ab)*/).length || 4 != ".".split(/(.?)(.?)/).length || ".".split(/()()/).length > 1 || "".split(/.?/).length) {
                    var u = void 0 === /()??/.exec("")[1];
                    r = function (t, e) {
                        var n = String(this);
                        if (void 0 === t && 0 === e) return [];
                        if (!o(t)) return i.call(n, t, e);
                        var r, s, a, f, l, p = [],
                            d = (t.ignoreCase ? "i" : "") + (t.multiline ? "m" : "") + (t.unicode ? "u" : "") + (t.sticky ? "y" : ""),
                            h = 0,
                            v = void 0 === e ? 4294967295 : e >>> 0,
                            y = new RegExp(t.source, d + "g");
                        for (u || (r = new RegExp("^" + y.source + "$(?!\\s)", d));
                            (s = y.exec(n)) && !((a = s.index + s[0].length) > h && (p.push(n.slice(h, s.index)), !u && s.length > 1 && s[0].replace(r, function () {
                                for (l = 1; l < arguments.length - 2; l++) void 0 === arguments[l] && (s[l] = void 0)
                            }), s.length > 1 && s.index < n.length && c.apply(p, s.slice(1)), f = s[0].length, h = a, p.length >= v));) y.lastIndex === s.index && y.lastIndex++;
                        return h === n.length ? !f && y.test("") || p.push("") : p.push(n.slice(h)), p.length > v ? p.slice(0, v) : p
                    }
                } else "0".split(void 0, 0).length && (r = function (t, e) {
                    return void 0 === t && 0 === e ? [] : i.call(this, t, e)
                });
                return [
                    function (n, o) {
                        var i = t(this),
                            c = void 0 == n ? void 0 : n[e];
                        return void 0 !== c ? c.call(n, i, o) : r.call(String(i), n, o)
                    },
                    r
                ]
            })
        },
        function (t, e) {
            t.exports = function (t, e) {
                if (null == t) return {};
                var n, r, o = {},
                    i = Object.keys(t);
                for (r = 0; r < i.length; r++) n = i[r], e.indexOf(n) >= 0 || (o[n] = t[n]);
                return o
            }
        },
        function (t, e) {
            t.exports = function (t, e) {
                return {
                    value: e,
                    done: !!t
                }
            }
        },
        function (t, e, n) {
            "use strict";
            var r = n(32),
                o = n(9),
                i = n(10),
                c = n(2),
                u = n(22),
                s = n(62),
                a = n(38),
                f = n(63),
                l = n(1)("iterator"),
                p = !([].keys && "next" in [].keys()),
                d = function () {
                    return this
                };
            t.exports = function (t, e, n, h, v, y, m) {
                s(n, e, h);
                var g, b, x, _ = function (t) {
                        if (!p && t in E) return E[t];
                        switch (t) {
                        case "keys":
                        case "values":
                            return function () {
                                return new n(this, t)
                            }
                        }
                        return function () {
                            return new n(this, t)
                        }
                    },
                    w = e + " Iterator",
                    O = "values" == v,
                    S = !1,
                    E = t.prototype,
                    j = E[l] || E["@@iterator"] || v && E[v],
                    I = j || _(v),
                    P = v ? O ? _("entries") : I : void 0,
                    T = "Array" == e && E.entries || j;
                if (T && (x = f(T.call(new t))) !== Object.prototype && x.next && (a(x, w, !0), r || "function" == typeof x[l] || c(x, l, d)), O && j && "values" !== j.name && (S = !0, I = function () {
                    return j.call(this)
                }), r && !m || !p && !S && E[l] || c(E, l, I), u[e] = I, u[w] = d, v)
                    if (g = {
                        values: O ? I : _("values"),
                        keys: y ? I : _("keys"),
                        entries: P
                    }, m)
                        for (b in g) b in E || i(E, b, g[b]);
                    else o(o.P + o.F * (p || S), e, g);
                return g
            }
        },
        function (t, e, n) {
            "use strict";
            var r = n(33),
                o = n(16),
                i = n(38),
                c = {};
            n(2)(c, n(1)("iterator"), function () {
                return this
            }), t.exports = function (t, e, n) {
                t.prototype = r(c, {
                    next: o(1, n)
                }), i(t, e + " Iterator")
            }
        },
        function (t, e, n) {
            var r = n(4),
                o = n(39),
                i = n(18)("IE_PROTO"),
                c = Object.prototype;
            t.exports = Object.getPrototypeOf || function (t) {
                return t = o(t), r(t, i) ? t[i] : "function" == typeof t.constructor && t instanceof t.constructor ? t.constructor.prototype : t instanceof Object ? c : null
            }
        },
        function (t, e, n) {
            var r = n(39),
                o = n(21);
            n(65)("keys", function () {
                return function (t) {
                    return o(r(t))
                }
            })
        },
        function (t, e, n) {
            var r = n(9),
                o = n(13),
                i = n(7);
            t.exports = function (t, e) {
                var n = (o.Object || {})[t] || Object[t],
                    c = {};
                c[t] = e(n), r(r.S + r.F * i(function () {
                    n(1)
                }), "Object", c)
            }
        },
        function (t, e, n) {
            for (var r = n(36), o = n(21), i = n(10), c = n(0), u = n(2), s = n(22), a = n(1), f = a("iterator"), l = a("toStringTag"), p = s.Array, d = {
                CSSRuleList: !0,
                CSSStyleDeclaration: !1,
                CSSValueList: !1,
                ClientRectList: !1,
                DOMRectList: !1,
                DOMStringList: !1,
                DOMTokenList: !0,
                DataTransferItemList: !1,
                FileList: !1,
                HTMLAllCollection: !1,
                HTMLCollection: !1,
                HTMLFormElement: !1,
                HTMLSelectElement: !1,
                MediaList: !0,
                MimeTypeArray: !1,
                NamedNodeMap: !1,
                NodeList: !0,
                PaintRequestList: !1,
                Plugin: !1,
                PluginArray: !1,
                SVGLengthList: !1,
                SVGNumberList: !1,
                SVGPathSegList: !1,
                SVGPointList: !1,
                SVGStringList: !1,
                SVGTransformList: !1,
                SourceBufferList: !1,
                StyleSheetList: !0,
                TextTrackCueList: !1,
                TextTrackList: !1,
                TouchList: !1
            }, h = o(d), v = 0; v < h.length; v++) {
                var y, m = h[v],
                    g = d[m],
                    b = c[m],
                    x = b && b.prototype;
                if (x && (x[f] || u(x, f, p), x[l] || u(x, l, m), s[m] = p, g))
                    for (y in r) x[y] || i(x, y, r[y], !0)
            }
        },
        function (t, e, n) {
            var r = n(35),
                o = n(8);
            t.exports = function (t, e, n) {
                if (r(e)) throw TypeError("String#" + n + " doesn't accept regex!");
                return String(o(t))
            }
        },
        function (t, e, n) {
            var r = n(1)("match");
            t.exports = function (t) {
                var e = /./;
                try {
                    "/./" [t](e)
                } catch (n) {
                    try {
                        return e[r] = !1, !"/./" [t](e)
                    } catch (t) {}
                }
                return !0
            }
        },
        function (t, e, n) {
            "use strict";
            n.r(e);
            n(43), n(56);
            var r = n(3),
                o = n.n(r),
                i = (n(58), n(42)),
                c = n.n(i),
                u = (n(36), n(64), n(66), n(40), n(41), n(23)),
                s = n.n(u);
            Array.prototype.includes || (Array.prototype.includes = function (t) {
                if (null == this) throw new TypeError("Array.prototype.includes called on null or undefined");
                var e = Object(this),
                    n = parseInt(e.length, 10) || 0;
                if (0 === n) return !1;
                var r, o, i = parseInt(arguments[1], 10) || 0;
                for (i >= 0 ? r = i : (r = n + i) < 0 && (r = 0); r < n;) {
                    if (t === (o = e[r]) || t != t && o != o) return !0;
                    r++
                }
                return !1
            });
            var a = function t(e) {
                var n = this,
                    r = e.src,
                    o = e.retryTimes;
                s()(this, t), this.fetch = function () {
                    var t = document.createElement("img");
                    t.src = n.src;
                    var e = n;
                    t.onerror = function () {
                        t = null, e.retryCount++, e.retryCount > e.retryTimes ? e.callback(null) : setTimeout(function () {
                            e.fetch()
                        }, 1e3)
                    }, t.onload = function () {
                        e.callback(e.src)
                    }
                }, this.then = function (t) {
                    n.callback = t, n.retryCount = 1, n.fetch()
                }, this.src = r, this.retryTimes = o || 20
            };
            e.default = new function t() {
                var e = this;
                s()(this, t), this.baseUrl = "", this.choose_widget_opened = !1, this.chooseIFrame = null, this.style = "", this.device = "", this.urlTypeList = {
                    mobile: {
                        selector: "/select_files?",
                        save: "/select_destination?",
                        preview: "/open_preview?"
                    },
                    pc: {
                        selector: "/open/open_platform/file_selector?",
                        preview: "/open/open_platform/file_preview?",
                        save: "/open/open_platform/file_save?",
                        upload: "/open/open_platform/file_upload?",
                        saveFile: "/open/open_platform/file_selector?"
                    }
                }, this.createIFrame = function (t) {
                    e._setIframeStyle(t);
                    var n = document.createElement("iframe");
                    return n.setAttribute("id", "fangcloud_" + t.type), n.setAttribute("style", e.style), n.setAttribute("src", t.src), document.body.appendChild(n), n
                }, this._choose_handler = function (t) {
                    var n = e.options;
                    if (![e.baseUrl, "https://v2.fangcloud.com", "https://v2.fangcloud.net"].includes(t.origin)) throw new Error("The message source is incorrect, Please check your requestAddr ");
                    try {
                        var r = t.data && JSON.parse(t.data) || "";
                        if (r && "minimize" === r.type) return e.handleMinimize();
                        if (r && "maximize" === r.type) return e.handleMaximize();
                        r && !r.type || !r ? r ? n.success && n.success(r) : n.cancel && n.cancel() : r && r.type && ("close" === r.type ? n.cancel && n.cancel() : n.success && n.success(r.data)), e._closeChooser()
                    } catch (t) {
                        console.log(t)
                    }
                }, this._paramsMapping = function (t) {
                    var n = {
                            fileId: "mobile" === e.device ? "file_id" : "preview",
                            selectFileLimit: "selectFileMax",
                            selectBtnText: "confirmBtnText",
                            saveBtnText: "confirmBtnText",
                            selectBtnColor: "confirmBtnColor",
                            saveBtnColor: "confirmBtnColor"
                        },
                        r = {};
                    return Object.keys(t || {}).forEach(function (e) {
                        "function" != typeof e && n[e] ? r[n[e]] = t[e] : r[e] = t[e]
                    }), r
                }, this._choose = function (t) {
                    if (!e.choose_widget_opened) {
                        e._isMobile();
                        var n = e._paramsMapping(t);
                        e.options = n;
                        var r = n.environmentAddr,
                            i = n.loginAddr,
                            u = n.requestAddr,
                            s = (n.customDomain, n.type),
                            a = c()(n, ["environmentAddr", "loginAddr", "requestAddr", "customDomain", "type"]),
                            f = Object.keys(a).filter(function (t) {
                                return a[t] && "function" != typeof a[t]
                            }).map(function (t) {
                                return "".concat(t, "=").concat(a[t])
                            });
                        i ? e.baseUrl = i.split("/sso/login")[0] : r ? e.baseUrl = r : "mobile" === e.device ? e.baseUrl = n.customDomain && "https://".concat(n.customDomain) || "https://h5.fangcloud.com" : e.baseUrl = u.split("/auth/openapi_login")[0], e.chooseIFrame = e.createIFrame(o()({}, n, {
                            type: s,
                            src: (u || i) + (i ? "?redirect=" : "&redirect=") + encodeURIComponent(e.baseUrl + e.urlTypeList[e.device][n.type] + f.join("&") + "&origin=" + window.location.origin)
                        })), e.choose_widget_opened = !0, window.addEventListener("message", e._choose_handler, !1)
                    }
                }, this._closeChooser = function () {
                    null !== e.chooseIFrame && (document.body.removeChild(e.chooseIFrame), e.chooseIFrame = null, e.choose_widget_opened = !1, e.style = "", window.removeEventListener("message", e._choose_handler, !1))
                }, this._isMobile = function () {
                    navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i) ? e.device = "mobile" : e.device = "pc"
                }, this._setIframeStyle = function (t) {
                    if ("mobile" === e.device) return e.style = "position:absolute;z-index: 999;border: none;left: 0;top: 0;width: 100%;height: 100%;overflow: hidden;";
                    var n = "position:absolute;z-index: 999;",
                        r = t.width,
                        o = t.height,
                        i = Number(r) || 650,
                        c = Number(o) || 450,
                        u = Math.max(document.documentElement.clientWidth, window.innerWidth || 0),
                        s = Math.max(document.documentElement.clientHeight, window.innerHeight || 0),
                        a = Math.max((u - i) / 2, 0),
                        f = Math.max((s - c) / 2, 0);
                    n += "background-color: #fff; border: 1px solid #ddd; width:".concat(i, "px; height:").concat(c, "px; top:").concat(f, "px; left:").concat(a, "px; box-shadow: 0px 0px 4px #ddd;"), e.style = n
                }, this.handleMinimize = function () {
                    var t = e.options.onMinimize;
                    t && t(), e.chooseIFrame.setAttribute("style", "position:fixed; z-index: 999;right: 2px; bottom: 2px; height: 40px;width: 320px; box-shadow: 0px 0px 4px #ddd;border: none")
                }, this.handleMaximize = function () {
                    var t = e.options.onMaximize;
                    t && t(), e.chooseIFrame.setAttribute("style", e.style)
                }, this.closePreview = function () {
                    e._closeChooser()
                }, this.closeSelect = function () {
                    e._closeChooser()
                }, this.closeDestination = function () {
                    e._closeChooser()
                }, this.selectFile = function () {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                    if (t.success && "function" != typeof t.success) throw new Error("options.success is required, please check your params");
                    e._choose(o()({}, t, {
                        type: "selector"
                    }))
                }, this.previewFile = function () {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                    e._choose(o()({}, t, {
                        type: "preview"
                    }))
                }, this.uploadFile = function () {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                    if (t.success && "function" != typeof t.success) throw new Error("options.success is required, please check your params");
                    e._choose(o()({}, t, {
                        type: "upload"
                    }))
                }, this.saveFile = function () {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                    if (t.success && "function" != typeof t.success) throw new Error("options.success is required, please check your params");
                    e._choose(o()({}, t, {
                        type: "saveFile"
                    }))
                }, this.selectDestination = function () {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                    if (t.success && "function" != typeof t.success) throw new Error("options.success is required, please check your params");
                    e._choose(o()({}, t, {
                        type: "save"
                    }))
                }, this.getPreviewLink = function (t) {
                    return e.baseUrl + "/apps/files/open_share_link?file_id" + t
                }, this.getDownloadLink = function (t) {
                    return e.baseUrl + "/apps/files/download?file_id=" + t + "&from_open_platform=true"
                }, this.getThumbnail = function (t, n, r) {
                    var o = e.baseUrl + "/apps/representations/download?file_id=" + t + "&file_version_key=" + n + "&kind=" + r;
                    return new a(o)
                }
            }
        }
    ]).default
});