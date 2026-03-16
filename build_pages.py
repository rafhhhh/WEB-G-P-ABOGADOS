import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

header_match = re.search(r'(<header.*?</header>)', html, re.DOTALL)
header = header_match.group(1) if header_match else ""
header = header.replace('href="#servicios"', 'href="index.html#servicios"')
header = header.replace('href="#equipo"', 'href="index.html#equipo"')
header = header.replace('href="#testimonios"', 'href="index.html#testimonios"')
header = header.replace('href="#ubicacion"', 'href="index.html#ubicacion"')
header = header.replace('href="#evaluacion"', 'href="index.html#evaluacion"')
header = header.replace('href="#" class="brand"', 'href="index.html" class="brand"')

footer_match = re.search(r'(<!-- Detailed Footer -->.*?</footer>)', html, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""
scripts = """    <!-- Fixed WhatsApp -->
    <a href="https://wa.me/34629030475" class="float-wa" aria-label="WhatsApp">
        <i class="ri-whatsapp-fill"></i>
    </a>
    <script src="./script.js"></script>
    <script>
        function toggleLlamanosMenu(e) { e.stopPropagation(); const wrap = e.currentTarget.closest('.btn-llamanos-wrap'); wrap.classList.toggle('open'); }
        document.addEventListener('click', function () { document.querySelectorAll('.btn-llamanos-wrap.open').forEach(function (el) { el.classList.remove('open'); }); });
    </script>"""
footer = footer_html + "\n" + scripts

# ─── TEMPLATE: "Otras Especialidades" (divorcios, penal, etc.) ───
template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | González & Pulido Abogados</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
    <link rel="stylesheet" href="./styles.css?v=3">
    <style>
        .inner-page-hero {{
            padding: 10rem 0 6rem;
            position: relative;
            background: linear-gradient(to bottom, rgba(61, 82, 101, 0.05) 0%, rgba(212, 175, 55, 0.05) 100%);
            text-align: center;
        }}
        .inner-page-title {{
            font-size: 4rem;
            margin-bottom: 1.5rem;
            color: var(--text-main);
        }}

        /* ── Stats Bar ── */
        .stats-bar {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1.5rem;
            margin-top: -2.5rem;
            position: relative;
            z-index: 11;
            padding: 0 1rem;
        }}
        .stat-card {{
            background: #FFF;
            border: 1px solid var(--border-light);
            border-radius: 14px;
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: 0 8px 30px rgba(0,0,0,0.07);
            transition: var(--transition);
            opacity: 0;
            transform: translateY(20px);
        }}
        .stat-card.revealed {{
            opacity: 1;
            transform: translateY(0);
        }}
        .stat-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 35px rgba(212,175,55,0.15);
            border-color: var(--gold);
        }}
        .stat-number {{
            font-family: var(--font-heading);
            font-size: 2.8rem;
            font-weight: 700;
            color: var(--gold);
            line-height: 1;
            margin-bottom: 0.4rem;
        }}
        .stat-label {{
            font-size: 0.9rem;
            color: var(--text-dim);
            font-weight: 500;
            letter-spacing: 0.02em;
        }}

        /* ── Content Section ── */
        .inner-content-section {{
            padding: 3rem 0 0;
        }}
        .content-card {{
            background: #FFFFFF;
            border: 1px solid var(--border-light);
            border-radius: 16px;
            padding: 4rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            position: relative;
            z-index: 10;
        }}
        .section-title {{
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .section-title i {{
            color: var(--gold);
            font-size: 1.6rem;
        }}
        .content-list {{
            list-style: none;
            padding: 0;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        .content-list li {{
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            background: rgba(212,175,55,0.03);
            padding: 1.5rem;
            border-radius: 12px;
            border: 1px solid rgba(212,175,55,0.1);
            transition: var(--transition);
        }}
        .content-list li:hover {{
            background: rgba(212,175,55,0.08);
            transform: translateY(-3px);
            box-shadow: 0 5px 20px rgba(212,175,55,0.15);
            border-color: var(--gold);
        }}
        .content-list i {{
            color: var(--gold);
            font-size: 1.8rem;
            margin-top: -0.2rem;
        }}

        /* ── Process Timeline ── */
        .process-section {{
            margin-top: 4rem;
            border-top: 1px solid var(--border-light);
            padding-top: 3rem;
        }}
        .timeline {{
            position: relative;
            padding-left: 2.5rem;
            margin-top: 2rem;
        }}
        .timeline::before {{
            content: '';
            position: absolute;
            left: 23px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, var(--gold), rgba(212,175,55,0.15));
        }}
        .timeline-item {{
            position: relative;
            margin-bottom: 2.5rem;
            padding-left: 2.5rem;
            opacity: 0;
            transform: translateX(-15px);
            transition: opacity 0.5s ease, transform 0.5s ease;
        }}
        .timeline-item.tl-visible {{
            opacity: 1;
            transform: translateX(0);
        }}
        .timeline-item::before {{
            content: attr(data-step);
            position: absolute;
            left: -2.5rem;
            top: 0;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: var(--gold);
            color: #FFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.1rem;
            box-shadow: 0 5px 15px rgba(212,175,55,0.3);
            z-index: 2;
        }}
        .timeline-item h4 {{
            font-size: 1.15rem;
            margin-bottom: 0.3rem;
            font-family: var(--font-ui);
            font-weight: 600;
            color: var(--text-main);
        }}
        .timeline-item p {{
            color: var(--text-dim);
            font-size: 0.95rem;
            line-height: 1.6;
        }}

        /* ── Highlights / Why Us ── */
        .highlights-section {{
            margin-top: 4rem;
            border-top: 1px solid var(--border-light);
            padding-top: 3rem;
        }}
        .highlights-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        .highlight-card {{
            background: linear-gradient(135deg, rgba(61,82,101,0.04) 0%, rgba(212,175,55,0.06) 100%);
            border: 1px solid rgba(212,175,55,0.12);
            border-radius: 14px;
            padding: 2rem;
            text-align: center;
            transition: var(--transition);
        }}
        .highlight-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(212,175,55,0.12);
            border-color: var(--gold);
        }}
        .highlight-card i {{
            font-size: 2.2rem;
            color: var(--gold);
            margin-bottom: 1rem;
            display: block;
        }}
        .highlight-card h4 {{
            font-family: var(--font-ui);
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 0.5rem;
        }}
        .highlight-card p {{
            font-size: 0.9rem;
            color: var(--text-dim);
            line-height: 1.55;
        }}

        /* ── FAQ Accordion ── */
        .faq-section {{
            margin-top: 4rem;
            border-top: 1px solid var(--border-light);
            padding-top: 3rem;
        }}
        .faq-list {{
            margin-top: 1.5rem;
        }}
        .faq-item {{
            border: 1px solid var(--border-light);
            border-radius: 12px;
            margin-bottom: 0.75rem;
            overflow: hidden;
            transition: var(--transition);
        }}
        .faq-item:hover {{
            border-color: rgba(212,175,55,0.3);
        }}
        .faq-item.active {{
            border-color: var(--gold);
            box-shadow: 0 4px 20px rgba(212,175,55,0.1);
        }}
        .faq-question {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1.25rem 1.5rem;
            cursor: pointer;
            background: transparent;
            border: none;
            width: 100%;
            text-align: left;
            font-family: var(--font-ui);
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            gap: 1rem;
            transition: var(--transition);
        }}
        .faq-question:hover {{
            background: rgba(212,175,55,0.04);
        }}
        .faq-question i {{
            color: var(--gold);
            font-size: 1.2rem;
            transition: transform 0.3s ease;
            flex-shrink: 0;
        }}
        .faq-item.active .faq-question i {{
            transform: rotate(180deg);
        }}
        .faq-answer {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s cubic-bezier(0.16,1,0.3,1), padding 0.3s ease;
            padding: 0 1.5rem;
        }}
        .faq-item.active .faq-answer {{
            max-height: 300px;
            padding: 0 1.5rem 1.25rem;
        }}
        .faq-answer p {{
            color: var(--text-dim);
            font-size: 0.95rem;
            line-height: 1.7;
        }}

        /* ── CTA Banner ── */
        .cta-banner {{
            margin-top: 4rem;
            background: linear-gradient(135deg, #3d5265 0%, #2a3a4a 100%);
            border-radius: 16px;
            padding: 3.5rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        .cta-banner::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 300px;
            height: 300px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(212,175,55,0.15), transparent 70%);
            pointer-events: none;
        }}
        .cta-banner h3 {{
            font-size: 2rem;
            color: #FFF;
            margin-bottom: 0.75rem;
        }}
        .cta-banner > p {{
            color: rgba(255,255,255,0.7);
            font-size: 1.05rem;
            max-width: 550px;
            margin: 0 auto 2rem;
            line-height: 1.6;
        }}
        .cta-banner .btn-solid-gold {{
            position: relative;
            z-index: 2;
        }}

        /* ── Bottom spacer ── */
        .inner-bottom-spacer {{
            padding-bottom: 6rem;
        }}

        @media (max-width: 768px) {{
            .inner-page-title {{ font-size: 2.5rem; }}
            .content-card {{ padding: 2rem 1.25rem; }}
            .stats-bar {{ grid-template-columns: repeat(2, 1fr); gap: 0.75rem; margin-top: -1.5rem; padding: 0 0.5rem; }}
            .stat-card {{ padding: 1.25rem 1rem; }}
            .stat-number {{ font-size: 2rem; }}
            .highlights-grid {{ grid-template-columns: 1fr; }}
            .cta-banner {{ padding: 2.5rem 1.5rem; }}
            .cta-banner h3 {{ font-size: 1.5rem; }}
            .timeline {{ padding-left: 2rem; }}
            .timeline-item {{ padding-left: 2rem; }}
        }}
    </style>
</head>
<body>


    {header}

    <main>
        <section class="inner-page-hero">
            <div class="container reveal-up">
                <span class="sub-heading">{icon} Especialidad</span>
                <h1 class="inner-page-title">{title}</h1>
                <p class="hero-desc" style="margin: 0 auto; max-width: 700px; color: var(--text-dim); font-size: 1.15rem;">{desc}</p>
            </div>
        </section>

        <!-- Stats Bar -->
        <section class="container">
            <div class="stats-bar" id="stats-bar">
                {stats_html}
            </div>
        </section>

        <section class="inner-content-section">
            <div class="container">
                <div class="content-card reveal-up">
                    <h2 class="section-title"><i class="ri-briefcase-line"></i> Nuestros Servicios</h2>
                    <ul class="content-list">
                        {services_html}
                    </ul>

                    <!-- Process Timeline -->
                    <div class="process-section">
                        <h2 class="section-title"><i class="ri-route-line"></i> {process_title}</h2>
                        <div class="timeline" id="process-timeline">
                            {steps_html}
                        </div>
                    </div>

                    <!-- Why Choose Us -->
                    <div class="highlights-section">
                        <h2 class="section-title"><i class="ri-award-line"></i> ¿Por qué elegirnos?</h2>
                        <div class="highlights-grid">
                            {highlights_html}
                        </div>
                    </div>

                    <!-- FAQ Accordion -->
                    <div class="faq-section">
                        <h2 class="section-title"><i class="ri-question-answer-line"></i> Preguntas Frecuentes</h2>
                        <div class="faq-list" id="faq-list">
                            {faq_html}
                        </div>
                    </div>

                    <!-- CTA Banner -->
                    <div class="cta-banner">
                        <h3>¿Necesitas asesoramiento?</h3>
                        <p>Primera consulta gratuita y sin compromiso. Analizamos tu caso y te orientamos sobre la mejor estrategia.</p>
                        <a href="index.html#evaluacion" class="btn-solid-gold" style="font-size: 1.1rem; padding: 1.2rem 2.5rem;">Estudiamos tu caso gratis <i class="ri-arrow-right-line"></i></a>
                    </div>
                </div>
            </div>
        </section>
        <div class="inner-bottom-spacer"></div>
    </main>

    {footer}

    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        // ── Stats counter animation ──
        var statsBar = document.getElementById('stats-bar');
        if (statsBar) {{
            var statsObserver = new IntersectionObserver(function(entries) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        var cards = statsBar.querySelectorAll('.stat-card');
                        cards.forEach(function(card, i) {{
                            setTimeout(function() {{
                                card.classList.add('revealed');
                            }}, i * 120);
                        }});
                        statsBar.querySelectorAll('.stat-counter').forEach(function(el) {{
                            var target = parseInt(el.getAttribute('data-target'));
                            var suffix = el.getAttribute('data-suffix') || '';
                            var prefix = el.getAttribute('data-prefix') || '';
                            var duration = 1800;
                            var startTime = null;
                            function ease(t) {{ return t < 0.5 ? 4*t*t*t : 1 - Math.pow(-2*t+2, 3)/2; }}
                            function animate(ts) {{
                                if (!startTime) startTime = ts;
                                var progress = Math.min((ts - startTime) / duration, 1);
                                var val = Math.floor(ease(progress) * target);
                                el.textContent = prefix + val.toLocaleString('es-ES') + suffix;
                                if (progress < 1) requestAnimationFrame(animate);
                                else el.textContent = prefix + target.toLocaleString('es-ES') + suffix;
                            }}
                            requestAnimationFrame(animate);
                        }});
                        statsObserver.unobserve(entry.target);
                    }}
                }});
            }}, {{ rootMargin: '0px 0px -50px 0px' }});
            statsObserver.observe(statsBar);
        }}

        // ── Timeline scroll reveal ──
        var timelineItems = document.querySelectorAll('.timeline-item');
        if (timelineItems.length) {{
            var tlObserver = new IntersectionObserver(function(entries) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('tl-visible');
                        tlObserver.unobserve(entry.target);
                    }}
                }});
            }}, {{ rootMargin: '0px 0px -60px 0px' }});
            timelineItems.forEach(function(item) {{ tlObserver.observe(item); }});
        }}

        // ── FAQ Accordion ──
        document.querySelectorAll('.faq-question').forEach(function(btn) {{
            btn.addEventListener('click', function() {{
                var item = btn.closest('.faq-item');
                var wasActive = item.classList.contains('active');
                document.querySelectorAll('.faq-item.active').forEach(function(el) {{
                    el.classList.remove('active');
                }});
                if (!wasActive) item.classList.add('active');
            }});
        }});
    }});
    </script>
</body>
</html>
"""

# ─── TEMPLATE: Extranjería (trámite individual) ───
extranjeria_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | González & Pulido Abogados</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">
    <link rel="stylesheet" href="./styles.css?v=3">
    <style>
        .inner-page-hero {{
            padding: 10rem 0 5rem;
            position: relative;
            background: linear-gradient(135deg, rgba(61,82,101,0.06) 0%, rgba(212,175,55,0.06) 100%);
            text-align: center;
        }}
        .inner-page-title {{
            font-size: 3.2rem;
            margin-bottom: 1rem;
            color: var(--text-main);
            line-height: 1.15;
        }}
        .breadcrumb {{
            display: inline-flex;
            align-items: center;
            gap: .5rem;
            font-size: .95rem;
            color: var(--text-dim);
            margin-bottom: 1.5rem;
        }}
        .breadcrumb a {{
            color: var(--gold);
            text-decoration: none;
            font-weight: 500;
        }}
        .breadcrumb a:hover {{ text-decoration: underline; }}
        .tagline {{
            font-size: 1.2rem;
            color: var(--text-dim);
            max-width: 650px;
            margin: 0 auto;
            line-height: 1.6;
        }}
        .tramite-content {{
            padding: 0 0 6rem;
        }}
        .tramite-card {{
            background: #FFF;
            border: 1px solid var(--border-light);
            border-radius: 16px;
            padding: 3.5rem 4rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            margin-top: -3rem;
            position: relative;
            z-index: 10;
        }}
        .tramite-section {{
            margin-bottom: 3rem;
        }}
        .tramite-section:last-child {{ margin-bottom: 0; }}
        .tramite-section-title {{
            font-size: 1.6rem;
            font-family: var(--font-heading);
            color: var(--text-main);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: .75rem;
        }}
        .tramite-section-title i {{
            color: var(--gold);
            font-size: 1.4rem;
        }}
        .tramite-text {{
            color: var(--text-dim);
            font-size: 1.05rem;
            line-height: 1.75;
        }}
        .req-list, .doc-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .req-list li, .doc-list li {{
            display: flex;
            align-items: flex-start;
            gap: .75rem;
            padding: 1rem 1.25rem;
            background: rgba(212,175,55,0.03);
            border: 1px solid rgba(212,175,55,0.1);
            border-radius: 10px;
            margin-bottom: .75rem;
            font-size: 1rem;
            color: var(--text-main);
            transition: var(--transition);
        }}
        .req-list li:hover, .doc-list li:hover {{
            background: rgba(212,175,55,0.08);
            border-color: var(--gold);
            transform: translateX(4px);
        }}
        .req-list li i, .doc-list li i {{
            color: var(--gold);
            font-size: 1.2rem;
            margin-top: 2px;
            flex-shrink: 0;
        }}
        .step-item {{
            display: flex;
            gap: 1.5rem;
            margin-bottom: 1.75rem;
            align-items: flex-start;
        }}
        .step-num {{
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: var(--gold);
            color: #FFF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1.1rem;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(212,175,55,0.3);
        }}
        .step-text h4 {{
            font-size: 1.1rem;
            margin-bottom: .15rem;
            font-family: var(--font-ui);
            font-weight: 600;
            color: var(--text-main);
        }}
        .step-text p {{
            color: var(--text-dim);
            font-size: .95rem;
            line-height: 1.5;
        }}
        .plazo-badge {{
            display: inline-flex;
            align-items: center;
            gap: .5rem;
            background: rgba(212,175,55,0.08);
            border: 1px solid rgba(212,175,55,0.25);
            border-radius: 12px;
            padding: 1rem 1.5rem;
            font-size: 1.1rem;
            font-weight: 500;
            color: var(--text-main);
        }}
        .plazo-badge i {{ color: var(--gold); font-size: 1.3rem; }}
        .divider {{
            border: none;
            border-top: 1px solid var(--border-light);
            margin: 2.5rem 0;
        }}
        @media (max-width: 768px) {{
            .inner-page-title {{ font-size: 2.2rem; }}
            .tramite-card {{ padding: 2rem 1.5rem; }}
            .tramite-section-title {{ font-size: 1.3rem; }}
        }}
    </style>
</head>
<body>
    {header}

    <main>
        <section class="inner-page-hero">
            <div class="container reveal-up">
                <div class="breadcrumb">
                    <a href="index.html">Inicio</a>
                    <i class="ri-arrow-right-s-line"></i>
                    <a href="index.html#especialidades">{category}</a>
                    <i class="ri-arrow-right-s-line"></i>
                    <span>{title}</span>
                </div>
                <h1 class="inner-page-title">{title}</h1>
                <p class="tagline">{tagline}</p>
            </div>
        </section>

        <section class="tramite-content">
            <div class="container reveal-up">
                <div class="tramite-card">

                    <div class="tramite-section">
                        <h2 class="tramite-section-title"><i class="ri-question-line"></i> ¿Qué es?</h2>
                        <p class="tramite-text">{que_es}</p>
                    </div>

                    <hr class="divider">

                    <div class="tramite-section">
                        <h2 class="tramite-section-title"><i class="ri-user-line"></i> ¿Quién puede solicitarlo?</h2>
                        <ul class="req-list">
                            {requisitos_html}
                        </ul>
                    </div>

                    <hr class="divider">

                    <div class="tramite-section">
                        <h2 class="tramite-section-title"><i class="ri-folder-line"></i> Documentación necesaria</h2>
                        <ul class="doc-list">
                            {documentos_html}
                        </ul>
                    </div>

                    <hr class="divider">

                    <div class="tramite-section">
                        <h2 class="tramite-section-title"><i class="ri-route-line"></i> ¿Cómo funciona el proceso?</h2>
                        {pasos_html}
                    </div>

                    <hr class="divider">

                    <div class="tramite-section">
                        <h2 class="tramite-section-title"><i class="ri-time-line"></i> ¿Cuánto tarda?</h2>
                        <div class="plazo-badge">
                            <i class="ri-calendar-check-line"></i>
                            {plazo}
                        </div>
                    </div>

                    <div style="text-align:center; margin-top:3.5rem;">
                        <a href="index.html#evaluacion" class="btn-solid-gold" style="font-size:1.1rem; padding:1.2rem 2.5rem;">
                            Estudiamos tu caso gratis <i class="ri-arrow-right-line"></i>
                        </a>
                    </div>

                </div>
            </div>
        </section>
    </main>

    {footer}
</body>
</html>
"""


# ══════════════════════════════════════════════════════════════
#  DATA: "Otras Especialidades" pages (existing)
# ══════════════════════════════════════════════════════════════
pages_data = [
    {
        "filename": "divorcios.html",
        "title": "Divorcios y Derecho de Familia",
        "icon": "<i class='ri-heart-2-line'></i>",
        "desc": "Te acompañamos legalmente en los momentos más difíciles, buscando la mejor resolución para ti y los tuyos. Cada caso familiar es único y merece un tratamiento cercano, discreto y profesional.",
        "services": [
            ("Divorcio express ante notario", "Resolución rápida y amistosa sin necesidad de juicio, ideal para parejas sin hijos ni bienes complejos."),
            ("Divorcio de mutuo acuerdo en juzgado", "Tramitación convencional pero pacífica, con convenio regulador pactado entre ambas partes."),
            ("Divorcio con hijos", "Gestión enfocada en la custodia, régimen de visitas, pensión alimenticia y bienestar de los menores."),
            ("Divorcios contenciosos", "Defensa sólida ante el juzgado cuando no hay acuerdo, protegiendo tus derechos e intereses."),
            ("Redacción de convenio regulador", "Acuerdos claros y justos que cubren custodia, pensiones, vivienda y reparto patrimonial."),
            ("Liquidación de bienes gananciales", "Reparto equitativo del patrimonio conyugal, incluyendo inmuebles, cuentas y deudas.")
        ],
        "stats": [
            (500, "+", "", "Divorcios gestionados"),
            (95, "", "%", "Acuerdos sin juicio"),
            (3, "", " meses", "Tiempo medio resolución"),
            (15, "+", "", "Años de experiencia")
        ],
        "process_title": "¿Cómo gestionamos tu divorcio?",
        "steps": [
            ("Consulta inicial gratuita", "Analizamos tu situación personal, patrimonial y familiar para definir la mejor estrategia legal."),
            ("Negociación del convenio", "Mediamos entre ambas partes para alcanzar un acuerdo justo sobre custodia, pensiones y bienes."),
            ("Redacción de documentos legales", "Preparamos el convenio regulador, la demanda y toda la documentación necesaria."),
            ("Tramitación ante juzgado o notario", "Presentamos la demanda o escritura y hacemos seguimiento del expediente hasta la sentencia."),
            ("Ejecución de la sentencia", "Nos aseguramos de que los acuerdos se cumplan: inscripciones, cambios de titularidad, pensiones, etc.")
        ],
        "highlights": [
            ("ri-emotion-line", "Trato cercano y humano", "Entendemos la carga emocional del proceso y te acompañamos con empatía y profesionalidad."),
            ("ri-shield-star-line", "Protección de los menores", "El bienestar de tus hijos es nuestra máxima prioridad en toda negociación y decisión."),
            ("ri-timer-flash-line", "Rapidez y eficacia", "Divorcios express en semanas, no en meses. Optimizamos cada paso del proceso."),
            ("ri-money-euro-circle-line", "Honorarios transparentes", "Sin sorpresas: presupuesto cerrado desde el primer día con facilidades de pago.")
        ],
        "faqs": [
            ("¿Cuánto tarda un divorcio de mutuo acuerdo?", "Un divorcio de mutuo acuerdo puede resolverse en 1 a 3 meses si ambas partes están de acuerdo. Ante notario, el proceso puede completarse en pocos días si no hay hijos menores."),
            ("¿Puedo divorciarme sin el consentimiento de mi pareja?", "Sí. En España no se necesita el consentimiento del otro cónyuge para divorciarse. En ese caso se tramita como divorcio contencioso ante el juzgado."),
            ("¿Qué pasa con la custodia de los hijos?", "Se puede acordar custodia compartida o exclusiva. Siempre se prioriza el interés superior del menor. Si no hay acuerdo, decide el juez con informe del equipo psicosocial."),
            ("¿Cómo se reparten los bienes en un divorcio?", "Depende del régimen económico matrimonial (gananciales o separación de bienes). En gananciales se reparten al 50% los bienes adquiridos durante el matrimonio."),
            ("¿Tiene coste la primera consulta?", "No. La primera consulta es completamente gratuita y sin compromiso. Evaluamos tu situación y te explicamos las opciones disponibles.")
        ]
    },
    {
        "filename": "derecho-bancario.html",
        "title": "Derecho Bancario",
        "icon": "<i class='ri-bank-line'></i>",
        "desc": "Protege tu dinero de abusos bancarios. Reclamamos intereses y cláusulas injustas y te ayudamos a cancelar tus deudas con la Ley de Segunda Oportunidad. Solo cobramos si ganamos.",
        "services": [
            ("Reclamación de tarjetas revolving", "Recupera los intereses usurarios pagados de más. Miles de sentencias favorables avalan esta reclamación."),
            ("Ley de Segunda Oportunidad", "Cancelación legal de deudas imposibles de pagar. Empezar de cero es posible con la legislación vigente."),
            ("Cláusulas suelo", "Reclamación de importes cobrados irregularmente en tu hipoteca por aplicación de un suelo mínimo."),
            ("Gastos hipotecarios y comisiones", "Recupera el dinero que el banco te cobró injustamente por apertura, tasación, notaría y registro."),
            ("Intereses de demora abusivos", "Defensa contra penalizaciones desproporcionadas en préstamos personales e hipotecarios.")
        ],
        "stats": [
            (2, "", " M€", "Recuperados para clientes"),
            (97, "", "%", "Casos ganados"),
            (800, "+", "", "Reclamaciones resueltas"),
            (0, "", "", "Coste inicial para ti")
        ],
        "process_title": "Nuestro modelo de trabajo",
        "steps": [
            ("Estudio gratuito del caso", "Analizamos tus contratos, recibos y extractos bancarios para determinar la viabilidad de la reclamación sin coste."),
            ("Reclamación extrajudicial", "Enviamos requerimiento formal al banco con cálculo de las cantidades a devolver, dando plazo para respuesta."),
            ("Negociación con la entidad", "Si el banco ofrece un acuerdo, evaluamos si es justo. Si no lo es, preparamos la demanda."),
            ("Demanda judicial", "Si el banco se niega o la oferta es insuficiente, presentamos demanda y defendemos tus intereses en tribunales."),
            ("Solo cobramos si ganamos", "Trabajamos a éxito: no pagas nada si no recuperamos tu dinero. Así de simple.")
        ],
        "highlights": [
            ("ri-hand-coin-line", "Sin coste si no ganamos", "Trabajamos a éxito en la mayoría de reclamaciones. Si no recuperas dinero, no nos debes nada."),
            ("ri-bar-chart-grouped-line", "Miles de sentencias favorables", "La jurisprudencia del Tribunal Supremo respalda las reclamaciones por abusos bancarios."),
            ("ri-calculator-line", "Cálculo exacto de tu reclamación", "Calculamos al céntimo lo que el banco te debe, con intereses legales incluidos."),
            ("ri-team-line", "Equipo especializado", "Abogados con formación específica en derecho bancario y consumo financiero.")
        ],
        "faqs": [
            ("¿Cuánto puedo recuperar por mi tarjeta revolving?", "Depende del importe pagado y los intereses aplicados, pero en la mayoría de casos se recuperan entre 3.000€ y 15.000€. Hacemos el cálculo exacto gratis."),
            ("¿Qué es la Ley de Segunda Oportunidad?", "Es un mecanismo legal que permite a personas físicas y autónomos cancelar sus deudas cuando no pueden pagarlas. Incluye un plan de pagos o la exoneración total de la deuda."),
            ("¿Puedo reclamar si ya pagué la hipoteca?", "Sí. Puedes reclamar gastos hipotecarios y cláusulas abusivas aunque ya hayas terminado de pagar tu hipoteca. El plazo de prescripción varía según el tipo de reclamación."),
            ("¿De verdad no pago nada si no gano?", "Correcto. En las reclamaciones bancarias trabajamos a éxito. Solo cobramos un porcentaje de lo que recuperamos para ti. Si no ganamos, no pagas."),
            ("¿Cuánto tarda una reclamación bancaria?", "La vía extrajudicial puede resolverse en 1-3 meses. Si hay que ir a juicio, el plazo se extiende a 6-12 meses dependiendo del juzgado.")
        ]
    },
    {
        "filename": "accidentes-trafico.html",
        "title": "Accidentes de Tráfico",
        "icon": "<i class='ri-car-line'></i>",
        "desc": "Obtén la máxima indemnización por tu accidente. Gestionamos íntegramente tu reclamación frente a aseguradoras, desde el parte hasta el cobro de la indemnización.",
        "services": [
            ("Accidentes de coche y moto", "Asesoramiento inmediato tras el siniestro para proteger tus derechos desde el primer momento."),
            ("Atropellos", "Defensa del peatón y ciclista, exigiendo la indemnización máxima por daños y lesiones."),
            ("Accidentes en transporte público", "Reclamación de lesiones sufridas en autobús, tren, taxi o VTC."),
            ("Indemnizaciones por lesiones", "Cálculo exacto del lucro cesante, secuelas temporales y permanentes según baremo actualizado."),
            ("Indemnizaciones por fallecimiento", "Apoyo total a familiares: gestión integral de indemnizaciones y tramitación de derechos."),
            ("Accidentes con fuga del responsable", "Reclamación al Consorcio de Compensación de Seguros cuando el causante huye o no tiene seguro.")
        ],
        "stats": [
            (350, "+", "", "Accidentes gestionados"),
            (98, "", "%", "Clientes indemnizados"),
            (45, "", "K€", "Indemnización media"),
            (0, "", "€", "Coste anticipado")
        ],
        "process_title": "Cómo gestionamos tu accidente",
        "steps": [
            ("Atención inmediata 24h", "Nos ponemos en contacto contigo desde el primer momento para asesorarte sobre qué hacer y qué no hacer."),
            ("Recopilación de pruebas", "Reunimos partes amistosos, informes policiales, informes médicos y toda documentación relevante."),
            ("Peritación médica y cálculo", "Evaluamos tus lesiones con peritos médicos y calculamos la indemnización máxima según el baremo vigente."),
            ("Reclamación a la aseguradora", "Presentamos oferta motivada a la compañía de seguros con cálculo detallado de todos los daños."),
            ("Negociación y cobro", "Negociamos la mejor cifra posible. Si la aseguradora no es justa, demandamos sin coste adicional para ti.")
        ],
        "highlights": [
            ("ri-24-hours-line", "Atención 24 horas", "Asistencia inmediata tras el accidente, incluyendo fines de semana y festivos."),
            ("ri-hand-coin-line", "Solo cobramos si cobras", "Sin gastos anticipados. Nuestros honorarios van ligados a tu indemnización."),
            ("ri-stethoscope-line", "Peritos médicos propios", "Valoramos tus lesiones con expertos independientes para maximizar tu indemnización."),
            ("ri-scales-3-line", "Experiencia en juicios", "Si la aseguradora no paga lo justo, acudimos a tribunales con un historial de sentencias favorables.")
        ],
        "faqs": [
            ("¿Qué hago justo después de un accidente?", "Lo primero es atender a los heridos y llamar a emergencias. Después, no firmes nada de la aseguradora contraria, toma fotos y llámanos. Te orientamos en cada paso."),
            ("¿Puedo reclamar si el accidente fue parcialmente mi culpa?", "Sí. Incluso con culpa compartida puedes obtener una indemnización proporcional a la responsabilidad del otro conductor."),
            ("¿Cuánto puedo recibir de indemnización?", "Depende de la gravedad de las lesiones, días de baja, secuelas y perjuicios económicos. El baremo de tráfico establece las cuantías mínimas."),
            ("¿Cuánto tarda en resolverse una reclamación?", "Por vía extrajudicial, 3 a 6 meses. Si hay que ir a juicio, puede extenderse 12-18 meses. Intentamos siempre la vía más rápida."),
            ("¿Y si el otro conductor no tiene seguro?", "Puedes reclamar al Consorcio de Compensación de Seguros, que cubre estos supuestos. Nosotros gestionamos el trámite completo.")
        ]
    },
    {
        "filename": "derecho-penal.html",
        "title": "Derecho Penal",
        "icon": "<i class='ri-shield-line'></i>",
        "desc": "Defensa penal impecable y experta. Representamos tus intereses tanto en la defensa ante acusaciones como ejerciendo la acusación particular, con total confidencialidad y disponibilidad.",
        "services": [
            ("Asistencia en comisaría y juzgado", "Atención rápida las 24 horas del día en caso de detención, con presencia inmediata del abogado."),
            ("Delitos económicos y societarios", "Estafas, fraudes, apropiación indebida, insolvencias punibles y delitos fiscales."),
            ("Violencia de género y sexual", "Representación legal especializada, sensible y confidencial, tanto para víctimas como para acusados."),
            ("Delitos en internet y ciberdelincuencia", "Estafas online, phishing, suplantación de identidad, delitos contra el honor en redes sociales."),
            ("Delitos contra la seguridad vial", "Alcoholemias, conducción temeraria, sin carnet, exceso de velocidad y negativa a someterse a pruebas."),
            ("Delitos de lesiones, amenazas y coacciones", "Defensa y acusación rigurosa en agresiones, amenazas y acoso.")
        ],
        "stats": [
            (400, "+", "", "Casos penales defendidos"),
            (92, "", "%", "Sentencias favorables"),
            (24, "", "h", "Disponibilidad garantizada"),
            (15, "+", "", "Años en derecho penal")
        ],
        "process_title": "¿Cómo actuamos en tu defensa?",
        "steps": [
            ("Asistencia inmediata", "Si estás detenido, acudimos a comisaría o juzgado de guardia de forma urgente para garantizar tus derechos."),
            ("Análisis exhaustivo del caso", "Estudiamos el atestado, las diligencias policiales y toda la documentación para diseñar la mejor estrategia."),
            ("Diseño de estrategia defensiva", "Elaboramos una defensa personalizada: nulidad de pruebas, atenuantes, conformidad ventajosa o juicio oral."),
            ("Actuación en juicio", "Comparecemos con preparación meticulosa, interrogamos testigos y presentamos pruebas a tu favor."),
            ("Seguimiento post-sentencia", "Gestionamos recursos, indultos o ejecución de la sentencia según el resultado obtenido.")
        ],
        "highlights": [
            ("ri-24-hours-line", "Disponibilidad 24/7", "Atención urgente en detenciones a cualquier hora, cualquier día del año."),
            ("ri-spy-line", "Máxima confidencialidad", "Tu caso se trata con absoluta reserva y secreto profesional."),
            ("ri-sword-line", "Defensa y acusación", "Experiencia tanto defendiendo a acusados como ejerciendo la acusación particular para víctimas."),
            ("ri-lightbulb-flash-line", "Estrategia personalizada", "Cada caso penal es diferente. Diseñamos una defensa a medida de tu situación.")
        ],
        "faqs": [
            ("¿Qué hago si me detiene la policía?", "Tienes derecho a guardar silencio y a que esté presente un abogado. No declares nada hasta que llegue tu abogado. Llámanos y acudimos de inmediato."),
            ("¿Cuánto cuesta la defensa penal?", "Depende de la complejidad del caso. Ofrecemos una primera consulta gratuita y un presupuesto cerrado antes de aceptar el caso."),
            ("¿Pueden condenarme si soy inocente?", "Es posible pero improbable si cuentas con una defensa sólida. Nuestro trabajo es demostrar tu inocencia con pruebas y argumentos jurídicos contundentes."),
            ("¿Qué es una conformidad penal?", "Es un acuerdo con la Fiscalía para aceptar una pena reducida a cambio de reconocer los hechos. Solo la recomendamos cuando es la opción más favorable para ti."),
            ("¿Puedo denunciar si soy víctima de un delito?", "Sí. Como acusación particular te acompañamos en todo el proceso: denuncia, instrucción, juicio y ejecución de la sentencia.")
        ]
    },
    {
        "filename": "gestion-inmobiliaria.html",
        "title": "Gestión Inmobiliaria",
        "icon": "<i class='ri-building-2-line'></i>",
        "desc": "Seguridad legal en tus inversiones inmobiliarias. Asesoramos en compraventas, alquileres y gestión patrimonial asegurando la máxima protección jurídica en cada operación.",
        "services": [
            ("Asesoramiento en compraventa", "Revisión exhaustiva de contratos de arras, escrituras públicas, cargas registrales y due diligence."),
            ("Arrendamientos y desahucios", "Redacción de contratos de alquiler seguros, gestión de impagos y tramitación de desahucios."),
            ("Gestión patrimonial", "Optimización legal y fiscal del patrimonio inmobiliario: sociedades, herencias y planificación."),
            ("Propiedad horizontal", "Resolución de conflictos en comunidades de vecinos, impugnación de acuerdos y reclamación de derramas."),
            ("Comunidad de bienes y proindivisos", "División de la cosa común, subastas voluntarias y extinciones de condominio."),
            ("Inscripciones registrales", "Liquidación de impuestos, herencias, donaciones e inscripciones en el Registro de la Propiedad.")
        ],
        "stats": [
            (300, "+", "", "Operaciones inmobiliarias"),
            (50, "+", "", "M€ asesorados"),
            (100, "", "%", "Operaciones con éxito"),
            (10, "+", "", "Años de experiencia")
        ],
        "process_title": "¿Cómo protegemos tu inversión?",
        "steps": [
            ("Análisis previo del inmueble", "Verificamos cargas registrales, situación urbanística, deudas de comunidad y estado legal del bien."),
            ("Revisión o redacción del contrato", "Preparamos o revisamos arras, contratos de compraventa o alquiler protegiendo tus intereses."),
            ("Negociación de condiciones", "Negociamos precio, plazos, cláusulas de penalización y condiciones especiales con la otra parte."),
            ("Acompañamiento en la firma", "Te acompañamos ante notario o en la firma privada para asegurar que todo esté en orden."),
            ("Gestión post-firma", "Liquidación de impuestos, cambio de titularidad, inscripción registral y alta de suministros.")
        ],
        "highlights": [
            ("ri-search-eye-line", "Due diligence completa", "Investigamos cada inmueble a fondo antes de que firmes nada: cargas, deudas, urbanismo."),
            ("ri-shield-check-line", "Contratos blindados", "Redactamos contratos que protegen tu inversión con cláusulas de garantía y penalización."),
            ("ri-money-euro-circle-line", "Optimización fiscal", "Minimizamos la carga impositiva de tus operaciones inmobiliarias dentro de la legalidad."),
            ("ri-home-heart-line", "Gestión integral", "Desde la búsqueda hasta la inscripción registral, nos encargamos de todo el proceso.")
        ],
        "faqs": [
            ("¿Necesito abogado para comprar una vivienda?", "No es legalmente obligatorio, pero sí muy recomendable. Un abogado verifica que el inmueble esté libre de cargas, revisa el contrato y protege tu inversión."),
            ("¿Qué son las arras y cuánto se paga?", "Las arras son una señal que confirma la intención de compra. Normalmente son el 10% del precio. Si el comprador se retira, las pierde; si se retira el vendedor, devuelve el doble."),
            ("¿Cuánto tarda un desahucio por impago?", "Depende del juzgado, pero un desahucio por impago de alquiler suele tardar entre 3 y 6 meses. Con nuestra gestión, intentamos siempre la vía más rápida."),
            ("¿Qué impuestos pago al comprar una vivienda?", "Si es nueva, IVA (10%) + AJD. Si es de segunda mano, ITP (varía por comunidad autónoma, entre 6% y 10%). Te asesoramos sobre los gastos exactos."),
            ("¿Pueden obligarme a vender mi parte de un proindiviso?", "Cualquier copropietario puede solicitar la división de la cosa común. Si no hay acuerdo, se puede solicitar judicialmente la venta en subasta.")
        ]
    },
    {
        "filename": "herencias.html",
        "title": "Herencias y Sucesiones",
        "icon": "<i class='ri-file-list-3-line'></i>",
        "desc": "Planificamos, tramitamos y gestionamos conflictos hereditarios para asegurar que el caudal relicto se divida de forma pacífica, justa y con el máximo beneficio fiscal.",
        "services": [
            ("Tramitación de la herencia", "Herencias testamentarias e intestadas (sin testamento), con gestión integral del expediente sucesorio."),
            ("Gestión de certificados", "Obtención de certificados de defunción, últimas voluntades, seguros de cobertura de vida y más."),
            ("Identificación e inventario", "Localización de herederos, investigación patrimonial y tasación profesional de todos los bienes."),
            ("Impuestos y sucesiones", "Liquidación optimizada de Plusvalía Municipal e Impuesto de Sucesiones aprovechando bonificaciones."),
            ("Conflictos familiares hereditarios", "Mediación, negociación y partición judicial del patrimonio cuando hay desacuerdos entre herederos."),
            ("Planificación sucesoria en vida", "Testamentos, donaciones y pactos sucesorios para que los herederos paguen el mínimo impositivo legal.")
        ],
        "stats": [
            (450, "+", "", "Herencias gestionadas"),
            (90, "", "%", "Resueltas sin litigio"),
            (30, "", "%", "Ahorro fiscal medio"),
            (12, "+", "", "Años de experiencia")
        ],
        "process_title": "¿Cómo gestionamos tu herencia?",
        "steps": [
            ("Estudio del testamento o declaración de herederos", "Analizamos si existe testamento, identificamos a los herederos legales y determinamos los derechos de cada uno."),
            ("Obtención de certificados oficiales", "Gestionamos certificado de defunción, últimas voluntades, seguros de vida y notas registrales."),
            ("Inventario y valoración de bienes", "Identificamos todos los bienes (inmuebles, cuentas, vehículos, deudas) y realizamos la tasación."),
            ("Negociación del reparto", "Mediamos entre los herederos para alcanzar un acuerdo justo, evitando conflictos y litigios."),
            ("Escritura de aceptación y adjudicación", "Formalizamos ante notario, liquidamos impuestos e inscribimos los bienes a nombre de cada heredero.")
        ],
        "highlights": [
            ("ri-emotion-happy-line", "Resolución sin conflictos", "El 90% de nuestras herencias se resuelven sin necesidad de acudir a tribunales."),
            ("ri-percent-line", "Optimización fiscal garantizada", "Aprovechamos todas las bonificaciones autonómicas para minimizar el Impuesto de Sucesiones."),
            ("ri-file-search-line", "Investigación patrimonial", "Localizamos cuentas, inmuebles, seguros y derechos que los herederos desconocen."),
            ("ri-time-line", "Plazos bajo control", "Controlamos los plazos fiscales (6 meses) para evitar recargos e intereses de demora.")
        ],
        "faqs": [
            ("¿Cuánto tiempo tengo para aceptar una herencia?", "El plazo para liquidar el Impuesto de Sucesiones es de 6 meses desde el fallecimiento, prorrogable 6 meses más. Es importante actuar con rapidez."),
            ("¿Puedo rechazar una herencia con deudas?", "Sí. Puedes renunciar a la herencia o aceptarla a beneficio de inventario, de modo que solo heredas si el activo supera las deudas."),
            ("¿Qué pasa si no hay testamento?", "Se realiza una declaración de herederos ante notario siguiendo el orden legal: hijos, cónyuge, padres, hermanos, etc."),
            ("¿Cuánto se paga de Impuesto de Sucesiones?", "Varía mucho según la comunidad autónoma, el parentesco y el valor de la herencia. En muchas comunidades, herencias entre padres e hijos tienen bonificaciones del 95-99%."),
            ("¿Puede un heredero bloquear el reparto?", "Sí, pero solo temporalmente. Si un heredero se niega a firmar, se puede solicitar la partición judicial para forzar el reparto.")
        ]
    }
]

# ══════════════════════════════════════════════════════════════
#  DATA: Extranjería pages (41 trámites individuales)
# ══════════════════════════════════════════════════════════════
extranjeria_data = [
    # ── NACIONALIDAD (6) ──
    {
        "filename": "nacionalidad-por-residencia.html",
        "category": "Nacionalidad",
        "title": "Nacionalidad Española por Residencia",
        "tagline": "La vía más habitual para obtener la nacionalidad española si llevas años viviendo legalmente en España.",
        "que_es": "Es el procedimiento que permite a los extranjeros que han residido en España de forma legal y continuada obtener la ciudadanía española. El tiempo de residencia exigido varía: 10 años como regla general, 5 años para refugiados, 2 años para nacionales de países iberoamericanos, Andorra, Filipinas, Guinea Ecuatorial, Portugal o sefardíes, y 1 año en casos especiales (nacidos en España, casados con español/a, viudo/a de español/a, etc.).",
        "quien": [
            "Extranjeros con residencia legal y continuada en España durante el tiempo exigido según su situación",
            "Personas con buena conducta cívica (sin antecedentes penales relevantes)",
            "Personas que demuestren suficiente grado de integración en la sociedad española"
        ],
        "documentos": [
            "Pasaporte completo en vigor",
            "Tarjeta de residencia (NIE) en vigor",
            "Certificado de nacimiento del país de origen (legalizado/apostillado y traducido)",
            "Certificado de antecedentes penales del país de origen",
            "Certificado de empadronamiento histórico",
            "Diploma DELE A2 o superior (acreditación de español)",
            "Diploma CCSE (prueba de conocimientos constitucionales y socioculturales)"
        ],
        "pasos": [
            ("Reunir documentación", "Recopilar todos los certificados, traducciones y legalizaciones necesarias."),
            ("Aprobar los exámenes DELE y CCSE", "Si no los tienes, preparar y superar las pruebas del Instituto Cervantes."),
            ("Presentar solicitud telemática", "Se presenta a través de la sede electrónica del Ministerio de Justicia."),
            ("Espera de resolución", "El Ministerio de Justicia estudia el expediente y emite resolución."),
            ("Jura o promesa de fidelidad al Rey", "Una vez concedida, se acude al Registro Civil para jurar y completar el trámite.")
        ],
        "plazo": "De 1 a 3 años desde la presentación de la solicitud"
    },
    {
        "filename": "nacionalidad-por-opcion.html",
        "category": "Nacionalidad",
        "title": "Nacionalidad Española por Opción",
        "tagline": "Si tienes un vínculo familiar directo con España, puedes optar por la nacionalidad española de forma más sencilla.",
        "que_es": "Es un derecho que permite a determinadas personas con lazos familiares o biográficos con España adquirir la nacionalidad sin necesidad de cumplir los plazos de residencia habituales. Se trata de un trámite más rápido y directo que la nacionalidad por residencia.",
        "quien": [
            "Personas que estén o hayan estado sujetas a la patria potestad de un español/a",
            "Nacidos en España de padres extranjeros, también nacidos en España (doble generación)",
            "Personas cuya filiación (padre o madre español/a) se determine después de los 18 años",
            "Adoptados mayores de 18 años por un ciudadano español (dentro de los 2 años siguientes a la adopción)"
        ],
        "documentos": [
            "Certificado de nacimiento del interesado (legalizado y traducido)",
            "Certificado de nacimiento del progenitor español o documento que acredite el vínculo",
            "DNI o pasaporte del progenitor español",
            "Certificado de empadronamiento",
            "Pasaporte del solicitante en vigor"
        ],
        "pasos": [
            ("Verificar que cumples los requisitos", "Confirmar que encajas en alguno de los supuestos de opción."),
            ("Reunir documentación", "Obtener y legalizar los certificados que acreditan tu derecho."),
            ("Presentar solicitud en el Registro Civil", "Acudir al Registro Civil del domicilio o al Consulado si estás fuera de España."),
            ("Resolución del encargado del Registro Civil", "El juez encargado valora la documentación y resuelve."),
            ("Jura o promesa e inscripción", "Formalización del acto y obtención del DNI español.")
        ],
        "plazo": "De 3 meses a 1 año aproximadamente"
    },
    {
        "filename": "nacionalidad-por-presuncion.html",
        "category": "Nacionalidad",
        "title": "Nacionalidad por Presunción",
        "tagline": "Podrías ser español/a sin saberlo. Si naciste en España en determinadas circunstancias, la ley te presume español.",
        "que_es": "La ley española presume la nacionalidad española de origen en ciertos casos, como los nacidos en España de padres desconocidos, los nacidos en España cuya nacionalidad de los padres no les transmite ninguna nacionalidad (apátridas), o los nacidos en España con filiación no determinada. Es una protección legal para evitar situaciones de apatridia.",
        "quien": [
            "Nacidos en territorio español de padres desconocidos",
            "Nacidos en España cuya legislación de los padres no les atribuye nacionalidad alguna",
            "Menores encontrados en territorio español cuyo lugar de nacimiento y filiación se desconocen"
        ],
        "documentos": [
            "Certificado literal de nacimiento inscrito en el Registro Civil español",
            "Documentación que acredite la situación de los padres (si se conocen)",
            "Informe o certificado que demuestre que no se ha adquirido otra nacionalidad",
            "Certificado de empadronamiento"
        ],
        "pasos": [
            ("Identificar tu situación", "Comprobar si encajas en uno de los supuestos de presunción."),
            ("Recopilar pruebas", "Obtener documentación del Registro Civil y, si aplica, certificados consulares."),
            ("Presentar solicitud en el Registro Civil", "Solicitar la declaración de nacionalidad española con valor de simple presunción."),
            ("Resolución del Registro Civil", "El encargado valora la documentación y declara la nacionalidad si procede.")
        ],
        "plazo": "De 3 a 6 meses aproximadamente"
    },
    {
        "filename": "nacionalidad-memoria-democratica.html",
        "category": "Nacionalidad",
        "title": "Nacionalidad por Ley de Memoria Democrática",
        "tagline": "Si eres descendiente de españoles que perdieron o tuvieron que renunciar a su nacionalidad por el exilio, esta ley es tu oportunidad.",
        "que_es": "La Ley 20/2022 de Memoria Democrática permite adquirir la nacionalidad española a los descendientes de quienes fueron exiliados por razones políticas, ideológicas o de creencia durante la Guerra Civil y la dictadura. También incluye a hijos nacidos en el extranjero de mujeres españolas que perdieron su nacionalidad al casarse con un extranjero antes de la Constitución de 1978.",
        "quien": [
            "Hijos/as e hijos/as de mujeres españolas que perdieron su nacionalidad por casarse con extranjeros antes de 1978",
            "Hijos/as de padres españoles de origen que perdieron o tuvieron que renunciar a la nacionalidad como consecuencia del exilio",
            "Nietos/as de españoles exiliados que perdieron la nacionalidad"
        ],
        "documentos": [
            "Certificado de nacimiento del solicitante (legalizado y traducido si procede)",
            "Certificado de nacimiento del progenitor/abuelo español de origen",
            "Documentación que acredite la condición de exiliado (pasaportes, registros de embarque, documentación de organismos internacionales de refugiados, etc.)",
            "Pasaporte del solicitante en vigor",
            "Certificado de matrimonio (cuando aplique para acreditar pérdida de nacionalidad por matrimonio)"
        ],
        "pasos": [
            ("Reunir documentación del vínculo familiar", "Localizar certificados de nacimiento y documentación histórica del familiar exiliado."),
            ("Presentar solicitud en Consulado o Registro Civil", "Según dónde residas, se presenta en el consulado español o en el Registro Civil."),
            ("Instrucción del expediente", "La autoridad comprueba los requisitos y la documentación."),
            ("Resolución favorable", "Si todo está en orden, se concede la nacionalidad española."),
            ("Jura o promesa e inscripción registral", "Se formaliza el acto y se inscribe como español.")
        ],
        "plazo": "De 6 meses a 2 años (la ley establece plazo máximo de 1 año, pero puede extenderse)"
    },
    {
        "filename": "agilizacion-nacionalidad.html",
        "category": "Nacionalidad",
        "title": "Agilización de Nacionalidad Española por Residencia",
        "tagline": "¿Tu expediente de nacionalidad lleva más de un año sin resolverse? Podemos acelerar el proceso legalmente.",
        "que_es": "Cuando el Ministerio de Justicia no resuelve una solicitud de nacionalidad en el plazo legalmente establecido, se puede instar la agilización del expediente mediante un requerimiento previo a la Administración y, si no responde, acudiendo a la vía judicial (recurso contencioso-administrativo por silencio). Es la herramienta legal para que tu expediente no quede olvidado.",
        "quien": [
            "Personas que hayan presentado solicitud de nacionalidad por residencia y no hayan recibido resolución tras 1 año",
            "Personas cuyo expediente esté paralizado sin justificación"
        ],
        "documentos": [
            "Copia del justificante de presentación de la solicitud de nacionalidad",
            "Copia del requerimiento previo enviado al Ministerio de Justicia",
            "Cualquier comunicación recibida del Ministerio sobre el estado del expediente"
        ],
        "pasos": [
            ("Comprobar el estado del expediente", "Verificar en la sede electrónica del Ministerio de Justicia que ha transcurrido más de 1 año."),
            ("Requerimiento previo a la Administración", "Enviar escrito instando al Ministerio a resolver en un plazo determinado."),
            ("Recurso contencioso-administrativo", "Si no hay respuesta, presentar demanda ante el Tribunal Superior de Justicia o Audiencia Nacional."),
            ("Sentencia favorable", "El juez obliga al Ministerio a resolver tu solicitud.")
        ],
        "plazo": "De 3 a 8 meses adicionales desde la interposición del recurso"
    },
    {
        "filename": "jura-nacionalidad-notario.html",
        "category": "Nacionalidad",
        "title": "Jura de Nacionalidad ante Notario",
        "tagline": "El último paso para ser español: la jura o promesa de fidelidad al Rey y a la Constitución.",
        "que_es": "Una vez que recibes la resolución favorable de concesión de nacionalidad, debes formalizar tu nuevo estatus mediante el acto de jura o promesa ante el encargado del Registro Civil. Desde las reformas recientes, también es posible realizar este trámite ante Notario, lo que agiliza notablemente los tiempos. Tras la jura se inscribe tu nacionalidad en el Registro Civil y puedes solicitar tu DNI.",
        "quien": [
            "Personas que hayan recibido resolución favorable de concesión de nacionalidad española",
            "Personas cuyo plazo de 180 días para realizar la jura no haya expirado"
        ],
        "documentos": [
            "Resolución de concesión de nacionalidad",
            "Pasaporte en vigor",
            "Certificado de nacimiento actualizado (legalizado y traducido)",
            "Certificado de empadronamiento actual",
            "Tasa correspondiente al trámite notarial"
        ],
        "pasos": [
            ("Recibir resolución favorable", "Confirmar que la concesión de nacionalidad ha sido aprobada."),
            ("Solicitar cita con Notario o Registro Civil", "Pedir cita para el acto de jura o promesa."),
            ("Acto de jura o promesa", "Jurar o prometer fidelidad al Rey y obediencia a la Constitución y las leyes."),
            ("Inscripción en el Registro Civil", "Se registra oficialmente la nacionalidad española."),
            ("Solicitar DNI español", "Acudir a la comisaría para tramitar tu primer DNI como ciudadano español.")
        ],
        "plazo": "De 1 a 3 meses desde la resolución favorable"
    },

    # ── VISADOS (6) ──
    {
        "filename": "visado-estancia-estudios.html",
        "category": "Visados",
        "title": "Visado de Estancia por Estudios",
        "tagline": "Estudia en España con la tranquilidad de tener todos tus papeles en regla desde el primer día.",
        "que_es": "Es el visado que permite a los extranjeros no comunitarios residir temporalmente en España para cursar estudios, realizar investigación, formación o prácticas no laborales. Autoriza la estancia mientras duren los estudios y puede permitir trabajar a tiempo parcial (máximo 20 horas semanales).",
        "quien": [
            "Personas admitidas en un centro de enseñanza autorizado en España",
            "Personas que cuenten con medios económicos suficientes para su estancia",
            "Personas con seguro médico en vigor que cubra toda la estancia"
        ],
        "documentos": [
            "Pasaporte con validez mínima durante toda la estancia",
            "Carta de admisión del centro educativo en España",
            "Acreditación de medios económicos suficientes (mínimo 100% del IPREM mensual)",
            "Seguro médico público o privado concertado con una entidad aseguradora autorizada",
            "Certificado de antecedentes penales del país de origen (si la estancia supera 6 meses)",
            "Certificado médico",
            "Justificante del pago de la tasa consular"
        ],
        "pasos": [
            ("Obtener admisión en el centro educativo", "Conseguir la carta de aceptación del centro donde vas a estudiar."),
            ("Solicitar el visado en el Consulado español", "Presentar toda la documentación en el consulado de tu país de residencia."),
            ("Esperar resolución consular", "El consulado estudia la solicitud y emite el visado."),
            ("Viajar a España y empadronarte", "Una vez en España, darte de alta en el padrón municipal."),
            ("Solicitar la TIE", "En los 30 días siguientes a la entrada, solicitar la Tarjeta de Identidad de Extranjero.")
        ],
        "plazo": "De 1 a 2 meses para la resolución del visado"
    },
    {
        "filename": "visado-residencia-no-lucrativa.html",
        "category": "Visados",
        "title": "Visado de Residencia No Lucrativa",
        "tagline": "Vive en España sin necesidad de trabajar, demostrando que cuentas con medios económicos suficientes.",
        "que_es": "Es el visado que permite residir en España a personas que disponen de medios económicos propios para mantenerse sin necesidad de trabajar. Ideal para jubilados, rentistas o personas con ahorros o ingresos pasivos. No autoriza a trabajar en España.",
        "quien": [
            "Personas que no sean ciudadanos de la UE/EEE",
            "Personas con medios económicos suficientes (aproximadamente 400% del IPREM mensual, unos 2.400€/mes)",
            "Personas sin antecedentes penales en los últimos 5 años",
            "Personas con seguro médico privado completo"
        ],
        "documentos": [
            "Pasaporte con validez mínima de 1 año",
            "Certificado de antecedentes penales del país de origen y de países donde se haya residido los últimos 5 años",
            "Certificado médico",
            "Acreditación de medios económicos (extractos bancarios, títulos de propiedad, pensiones, etc.)",
            "Seguro médico privado con cobertura completa en España",
            "Justificante del pago de la tasa consular"
        ],
        "pasos": [
            ("Reunir documentación económica", "Preparar extractos bancarios y justificantes de ingresos o patrimonio."),
            ("Solicitar el visado en el Consulado español", "Presentar la solicitud presencialmente en el consulado correspondiente."),
            ("Resolución consular", "El consulado evalúa la solvencia económica y la documentación."),
            ("Viajar a España", "Una vez concedido el visado, entrar en España en el plazo establecido."),
            ("Solicitar la TIE", "En el plazo de 1 mes desde la entrada, tramitar la Tarjeta de Identidad de Extranjero.")
        ],
        "plazo": "De 1 a 3 meses para la resolución del visado"
    },
    {
        "filename": "visado-familiar-ciudadano-ue.html",
        "category": "Visados",
        "title": "Visado de Familiar de Ciudadano de la UE",
        "tagline": "Si tu familiar es ciudadano europeo y quieres reunirte con él en España, este visado es tu camino.",
        "que_es": "Es el visado que permite a los familiares de ciudadanos de la Unión Europea, del EEE o de Suiza que no sean europeos entrar en España para residir junto a su familiar comunitario. Se tramita de forma preferente y gratuita.",
        "quien": [
            "Cónyuge o pareja de hecho registrada de un ciudadano de la UE",
            "Descendientes menores de 21 años o dependientes del ciudadano de la UE o de su cónyuge",
            "Ascendientes dependientes del ciudadano de la UE o de su cónyuge"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Documento que acredite la condición de ciudadano de la UE del familiar (DNI o pasaporte)",
            "Certificado de matrimonio o pareja de hecho registrada",
            "Documentación que acredite el parentesco (certificados de nacimiento)",
            "Documentación que acredite la dependencia económica (si aplica)"
        ],
        "pasos": [
            ("Reunir documentación del vínculo familiar", "Obtener y legalizar certificados de matrimonio o parentesco."),
            ("Solicitar visado en el Consulado", "Se tramita de forma preferente; no se paga tasa consular."),
            ("Resolución rápida", "El consulado debe resolver en plazo máximo de 15 días."),
            ("Viajar a España", "Entrar en territorio español con el visado concedido."),
            ("Solicitar Tarjeta de Familiar de Ciudadano de la UE", "Presentar solicitud en el plazo de 3 meses desde la entrada.")
        ],
        "plazo": "Máximo 15 días para la resolución del visado"
    },
    {
        "filename": "visado-familiar-ciudadano-espanol.html",
        "category": "Visados",
        "title": "Visado de Familiar de Ciudadano Español",
        "tagline": "Si tu cónyuge, pareja o familiar directo es español, puedes obtener el visado para vivir juntos en España.",
        "que_es": "Similar al visado de familiar de ciudadano de la UE, este visado se concede a los familiares directos de ciudadanos españoles que necesitan un visado para entrar en España. También se tramita de forma preferente y sin coste de tasa.",
        "quien": [
            "Cónyuge o pareja de hecho registrada de un ciudadano español",
            "Hijos menores de 21 años o dependientes del ciudadano español o de su cónyuge",
            "Ascendientes dependientes del ciudadano español o de su cónyuge"
        ],
        "documentos": [
            "Pasaporte en vigor del solicitante",
            "DNI del ciudadano español",
            "Certificado de matrimonio o inscripción de pareja de hecho",
            "Certificados de nacimiento que acrediten el parentesco",
            "Prueba de dependencia económica (si aplica, para ascendientes o hijos mayores de 21)"
        ],
        "pasos": [
            ("Acreditar vínculo familiar", "Obtener y preparar toda la documentación que demuestre la relación."),
            ("Presentar solicitud en el Consulado español", "Se tramita de forma gratuita y preferente."),
            ("Resolución rápida", "El consulado resuelve en un máximo de 15 días."),
            ("Viajar a España", "Entrar en España con el visado en vigor."),
            ("Solicitar Tarjeta de Familiar de Ciudadano de la UE", "En los 3 meses siguientes, tramitar la tarjeta de residencia.")
        ],
        "plazo": "Máximo 15 días para la resolución del visado"
    },
    {
        "filename": "visado-trabajo-cuenta-ajena.html",
        "category": "Visados",
        "title": "Visado de Residencia y Trabajo por Cuenta Ajena",
        "tagline": "El visado para venir a España con un contrato de trabajo ya firmado y empezar a trabajar desde el primer día.",
        "que_es": "Es el visado que se concede a los trabajadores extranjeros que cuentan con una autorización de residencia y trabajo tramitada por un empleador en España. El empresario debe gestionar primero la autorización ante la Oficina de Extranjería, y una vez concedida, el trabajador solicita el visado en el consulado de su país.",
        "quien": [
            "Trabajadores extranjeros no comunitarios con oferta de empleo en España",
            "Personas que no se encuentren en situación irregular en España",
            "Personas sin antecedentes penales en los últimos 5 años"
        ],
        "documentos": [
            "Pasaporte con validez mínima de 4 meses",
            "Autorización de residencia y trabajo concedida (tramitada por el empleador)",
            "Certificado de antecedentes penales del país de origen",
            "Certificado médico",
            "Justificante del pago de la tasa consular",
            "Contrato de trabajo firmado"
        ],
        "pasos": [
            ("El empleador solicita la autorización de trabajo", "La empresa presenta la solicitud ante la Oficina de Extranjería competente."),
            ("Resolución de la autorización", "La Oficina de Extranjería concede o deniega la autorización."),
            ("Solicitar el visado en el Consulado", "Con la autorización concedida, el trabajador solicita el visado en su país."),
            ("Viajar a España y darse de alta en la Seguridad Social", "Entrar en España e incorporarse al puesto de trabajo."),
            ("Solicitar la TIE", "En el plazo de 1 mes, tramitar la Tarjeta de Identidad de Extranjero.")
        ],
        "plazo": "De 2 a 4 meses en total (autorización + visado)"
    },
    {
        "filename": "visado-turista.html",
        "category": "Visados",
        "title": "Visado de Turista",
        "tagline": "Si necesitas visado para entrar en España como turista, te ayudamos a tramitarlo correctamente.",
        "que_es": "Es el visado de corta estancia (tipo C Schengen) que permite permanecer en España y en el espacio Schengen hasta un máximo de 90 días dentro de un periodo de 180 días. Es necesario para los ciudadanos de países que no tienen acuerdo de exención de visado con la UE.",
        "quien": [
            "Nacionales de países que requieren visado Schengen para estancias cortas",
            "Personas que puedan acreditar el propósito turístico del viaje",
            "Personas con medios económicos suficientes para la estancia y seguro de viaje"
        ],
        "documentos": [
            "Pasaporte con validez mínima de 3 meses posterior a la fecha de salida prevista",
            "Fotografías tipo carnet recientes",
            "Seguro médico de viaje con cobertura mínima de 30.000€",
            "Reserva de alojamiento o carta de invitación",
            "Acreditación de medios económicos (aprox. 108€/día)",
            "Reserva de billete de ida y vuelta",
            "Justificante del pago de la tasa consular (80€)"
        ],
        "pasos": [
            ("Solicitar cita en el Consulado o centro de visados", "Reservar cita a través de la web consular o del proveedor de servicios (BLS, VFS, etc.)."),
            ("Presentar documentación completa", "Acudir con toda la documentación original y copias."),
            ("Entrevista consular", "En algunos casos, el consulado puede requerir una entrevista personal."),
            ("Resolución", "El consulado resuelve en un plazo máximo de 15 días (ampliable a 45)."),
            ("Recoger el visado y viajar", "Si es favorable, recoger el pasaporte con el visado estampado y viajar.")
        ],
        "plazo": "De 15 a 45 días para la resolución"
    },

    # ── FAMILIARES (7) ──
    {
        "filename": "matrimonio-extranjeria.html",
        "category": "Familiares",
        "title": "Matrimonio",
        "tagline": "Te ayudamos con todos los trámites legales para que tu matrimonio en España sea válido y reconocido.",
        "que_es": "El matrimonio con implicaciones de extranjería incluye las uniones donde al menos uno de los cónyuges es extranjero. Requiere trámites adicionales como la legalización de documentos y, en muchos casos, una audiencia reservada ante el encargado del Registro Civil para verificar que no se trata de un matrimonio de conveniencia.",
        "quien": [
            "Parejas donde al menos uno de los cónyuges es extranjero",
            "Ambos deben ser mayores de edad (o menores emancipados)",
            "Ambos deben estar solteros o legalmente divorciados/viudos"
        ],
        "documentos": [
            "Certificado de nacimiento del cónyuge extranjero (legalizado/apostillado y traducido)",
            "Certificado de estado civil o soltería (legalizado y traducido)",
            "Certificado de empadronamiento",
            "Pasaporte o NIE del cónyuge extranjero",
            "DNI del cónyuge español (si aplica)",
            "Fe de vida y estado del cónyuge extranjero"
        ],
        "pasos": [
            ("Reunir documentación", "Obtener y legalizar todos los certificados del país de origen."),
            ("Presentar expediente matrimonial en el Registro Civil", "Iniciar el expediente en el Registro Civil del domicilio."),
            ("Audiencia reservada", "Entrevista separada a cada cónyuge para verificar la autenticidad del matrimonio."),
            ("Auto de aprobación", "El juez encargado del Registro Civil aprueba la celebración."),
            ("Celebración del matrimonio", "Acto civil o religioso según preferencia, con inscripción en el Registro Civil.")
        ],
        "plazo": "De 2 a 6 meses desde la presentación del expediente"
    },
    {
        "filename": "pareja-de-hecho.html",
        "category": "Familiares",
        "title": "Pareja de Hecho",
        "tagline": "Registra tu pareja de hecho en España y accede a los mismos derechos de reagrupación que el matrimonio.",
        "que_es": "La inscripción como pareja de hecho es una alternativa al matrimonio que permite formalizar una relación de convivencia estable. En el ámbito de extranjería, una pareja de hecho registrada tiene efectos similares al matrimonio para solicitar tarjetas de familiar de ciudadano de la UE o reagrupación familiar.",
        "quien": [
            "Parejas con relación de convivencia estable (generalmente más de 1 año)",
            "Ambos miembros deben ser mayores de edad",
            "Ninguno de los miembros puede estar casado o inscrito en otra pareja de hecho",
            "No pueden tener relación de parentesco directo entre sí"
        ],
        "documentos": [
            "Certificado de empadronamiento conjunto o prueba de convivencia",
            "Certificados de nacimiento de ambos miembros",
            "Pasaporte/DNI/NIE de ambos",
            "Certificado de estado civil (soltería o divorcio)",
            "Declaración jurada de no estar inscrito en otra pareja de hecho"
        ],
        "pasos": [
            ("Comprobar los requisitos de tu Comunidad Autónoma", "Cada comunidad tiene su propio registro y requisitos."),
            ("Reunir documentación", "Obtener certificados y pruebas de convivencia."),
            ("Presentar solicitud en el Registro de Parejas de Hecho", "Acudir al registro correspondiente de tu comunidad autónoma."),
            ("Resolución e inscripción", "Una vez verificada la documentación, se inscribe la pareja."),
            ("Solicitar tarjeta de residencia (si aplica)", "Con la inscripción, el miembro extranjero puede solicitar su tarjeta de familiar.")
        ],
        "plazo": "De 1 a 3 meses según la Comunidad Autónoma"
    },
    {
        "filename": "reagrupacion-familiar-ue.html",
        "category": "Familiares",
        "title": "Reagrupación Familiar de Ciudadano de la UE",
        "tagline": "Trae a tus familiares a España si eres ciudadano europeo. Un derecho comunitario fundamental.",
        "que_es": "Los ciudadanos de la Unión Europea que residen en España tienen derecho a que sus familiares directos (cónyuge, descendientes y ascendientes dependientes) puedan residir con ellos, aunque estos familiares no sean europeos. El familiar obtiene una Tarjeta de Familiar de Ciudadano de la UE que le permite residir y trabajar.",
        "quien": [
            "Cónyuge o pareja de hecho registrada del ciudadano de la UE",
            "Hijos menores de 21 años, o mayores dependientes, del ciudadano de la UE o de su cónyuge",
            "Padres dependientes del ciudadano de la UE o de su cónyuge"
        ],
        "documentos": [
            "Pasaporte del familiar en vigor",
            "DNI o pasaporte del ciudadano de la UE",
            "Certificado de inscripción del ciudadano de la UE en el Registro Central de Extranjeros",
            "Certificado de matrimonio, pareja de hecho o nacimiento que acredite el parentesco",
            "Prueba de dependencia económica (para ascendientes o hijos mayores de 21)"
        ],
        "pasos": [
            ("El familiar entra en España", "Con visado si lo necesita, o sin visado si su nacionalidad está exenta."),
            ("Solicitar Tarjeta de Familiar de Ciudadano UE", "Presentar solicitud en la Oficina de Extranjería en los 3 meses siguientes a la entrada."),
            ("Toma de huellas", "Acudir a la cita para la toma de huellas dactilares."),
            ("Resolución y obtención de la tarjeta", "Se concede la tarjeta con validez de 5 años, renovable.")
        ],
        "plazo": "De 1 a 3 meses para la resolución de la tarjeta"
    },
    {
        "filename": "familiar-ciudadano-espanol.html",
        "category": "Familiares",
        "title": "Familiar de Ciudadano Español",
        "tagline": "Si tu familiar directo es español, tienes derecho a residir y trabajar en España.",
        "que_es": "Los familiares directos de ciudadanos españoles (cónyuge, pareja de hecho, hijos y padres dependientes) que no sean europeos pueden obtener una tarjeta de residencia como familiar de ciudadano de la UE. Esta tarjeta permite residir y trabajar en España sin necesidad de autorización de trabajo independiente.",
        "quien": [
            "Cónyuge o pareja de hecho registrada del ciudadano español",
            "Hijos del ciudadano español o de su cónyuge (menores de 21 años o dependientes)",
            "Padres del ciudadano español o de su cónyuge que sean dependientes económicos"
        ],
        "documentos": [
            "Pasaporte en vigor del familiar extranjero",
            "DNI del ciudadano español",
            "Certificado de matrimonio o inscripción de pareja de hecho",
            "Certificados de nacimiento que acrediten el parentesco",
            "Prueba de convivencia o dependencia económica según el caso"
        ],
        "pasos": [
            ("Reunir documentación del vínculo", "Preparar certificados que demuestren la relación familiar."),
            ("Presentar solicitud en la Oficina de Extranjería", "Solicitar la tarjeta de familiar de ciudadano de la UE."),
            ("Cita de toma de huellas", "Acudir a la cita presencial con la documentación original."),
            ("Resolución y recogida de tarjeta", "Se concede tarjeta de residencia con validez de 5 años.")
        ],
        "plazo": "De 1 a 3 meses para la resolución"
    },
    {
        "filename": "reagrupacion-familiar-extranjero.html",
        "category": "Familiares",
        "title": "Reagrupación Familiar de Extranjero",
        "tagline": "Si resides legalmente en España, puedes traer a tu familia a vivir contigo.",
        "que_es": "Es el derecho que tienen los extranjeros con residencia legal en España a solicitar la autorización de residencia para que sus familiares directos (cónyuge, hijos y, en determinados supuestos, ascendientes) se reúnan con ellos. El reagrupante debe acreditar medios económicos y vivienda adecuada.",
        "quien": [
            "Extranjeros con autorización de residencia renovada (al menos 1 año de residencia y autorización renovada o de larga duración)",
            "Que dispongan de medios económicos suficientes para mantener a la familia",
            "Que cuenten con vivienda adecuada (certificada por informe municipal)"
        ],
        "documentos": [
            "Copia del pasaporte y tarjeta de residencia del reagrupante",
            "Acreditación de medios económicos (nóminas, contrato de trabajo, declaración de la renta)",
            "Informe de vivienda adecuada emitido por el ayuntamiento o comunidad autónoma",
            "Certificados de nacimiento y/o matrimonio que acrediten el parentesco",
            "Pasaporte del familiar a reagrupar",
            "Certificado de antecedentes penales del familiar (si es mayor de edad)"
        ],
        "pasos": [
            ("Obtener informe de vivienda adecuada", "Solicitar al ayuntamiento la acreditación de que la vivienda reúne condiciones."),
            ("Presentar solicitud de reagrupación en la Oficina de Extranjería", "El reagrupante presenta la solicitud en España."),
            ("Resolución de la autorización", "La Oficina de Extranjería resuelve si se cumplen los requisitos."),
            ("El familiar solicita el visado en el Consulado", "Una vez concedida la autorización, el familiar acude al consulado."),
            ("Entrada en España y solicitud de TIE", "El familiar viaja, se empadrona y solicita su tarjeta de residencia.")
        ],
        "plazo": "De 3 a 6 meses en total (autorización + visado)"
    },
    {
        "filename": "residencia-hijo-nacido-espana.html",
        "category": "Familiares",
        "title": "Residencia del Hijo de Residente Legal Nacido en España",
        "tagline": "Si tu hijo nació en España y tú tienes residencia legal, puede obtener su propia autorización de residencia.",
        "que_es": "Los hijos de extranjeros con residencia legal que nacen en territorio español tienen derecho a obtener una autorización de residencia. Este trámite es más sencillo que la reagrupación familiar, ya que el menor ya se encuentra en España y basta con acreditar la filiación y la residencia legal del progenitor.",
        "quien": [
            "Hijos menores de edad nacidos en España",
            "Al menos uno de los progenitores debe tener residencia legal en España",
            "La solicitud debe presentarse dentro del primer año de vida del menor (recomendado)"
        ],
        "documentos": [
            "Certificado literal de nacimiento del menor inscrito en el Registro Civil español",
            "Pasaporte del menor (si lo tiene) o certificado de la solicitud",
            "Tarjeta de residencia en vigor del progenitor",
            "Certificado de empadronamiento del menor",
            "Libro de familia o documento equivalente"
        ],
        "pasos": [
            ("Inscribir al menor en el Registro Civil", "Registrar el nacimiento en el plazo legal."),
            ("Reunir documentación", "Preparar certificado de nacimiento y documentación del progenitor."),
            ("Presentar solicitud en la Oficina de Extranjería", "Solicitar la autorización de residencia del menor."),
            ("Resolución y obtención de la TIE", "Se concede la autorización y se tramita la tarjeta del menor.")
        ],
        "plazo": "De 1 a 3 meses"
    },
    {
        "filename": "residencia-hijo-no-nacido-espana.html",
        "category": "Familiares",
        "title": "Residencia del Hijo de Residente Legal No Nacido en España",
        "tagline": "Si tu hijo no nació en España pero tú resides legalmente aquí, también puede obtener residencia.",
        "que_es": "Los hijos menores de extranjeros con residencia legal en España que no nacieron en territorio español pueden obtener autorización de residencia mediante reagrupación familiar. Este procedimiento requiere que el progenitor demuestre medios económicos y vivienda adecuada, similar al proceso general de reagrupación.",
        "quien": [
            "Hijos menores de edad de un progenitor con residencia legal en España",
            "El progenitor reagrupante debe tener autorización de residencia renovada o de larga duración",
            "El progenitor debe acreditar medios económicos suficientes y vivienda adecuada"
        ],
        "documentos": [
            "Certificado de nacimiento del menor (legalizado/apostillado y traducido)",
            "Pasaporte del menor en vigor",
            "Tarjeta de residencia del progenitor en vigor",
            "Acreditación de medios económicos del progenitor",
            "Informe de vivienda adecuada",
            "Consentimiento del otro progenitor (si no convive)"
        ],
        "pasos": [
            ("Obtener informe de vivienda adecuada", "Solicitar certificación al ayuntamiento."),
            ("Presentar solicitud de reagrupación", "El progenitor presenta la solicitud en la Oficina de Extranjería."),
            ("Resolución de la autorización", "La Oficina de Extranjería resuelve la solicitud."),
            ("El menor solicita visado en el Consulado", "Con la autorización concedida, se tramita el visado consular."),
            ("Entrada en España y solicitud de TIE", "El menor entra en España y se tramita su tarjeta de residencia.")
        ],
        "plazo": "De 3 a 6 meses en total (autorización + visado)"
    },

    # ── RESIDENCIAS (12) ──
    {
        "filename": "residencia-trabajo-cuenta-ajena.html",
        "category": "Residencias",
        "title": "Residencia y Trabajo por Cuenta Ajena",
        "tagline": "Trabaja legalmente en España con un contrato de trabajo. La autorización que necesitas para empezar tu vida laboral.",
        "que_es": "Es la autorización que permite a un extranjero no comunitario residir y trabajar en España por cuenta de un empleador. Debe ser solicitada por el empresario ante la Oficina de Extranjería y requiere que la situación nacional de empleo permita la contratación o que el trabajador esté en algún supuesto exceptuado.",
        "quien": [
            "Extranjeros no comunitarios con una oferta de empleo en España",
            "Personas sin antecedentes penales en España y en sus países de residencia anteriores",
            "Personas que no se encuentren irregularmente en España (salvo supuestos específicos)"
        ],
        "documentos": [
            "Pasaporte completo del trabajador",
            "Contrato de trabajo firmado por ambas partes",
            "Documentación acreditativa de la empresa (CIF, escrituras, TC1/TC2, declaración IRPF)",
            "Certificado de antecedentes penales del trabajador",
            "Titulación o acreditación profesional (si el puesto lo requiere)"
        ],
        "pasos": [
            ("El empresario presenta la solicitud", "Ante la Oficina de Extranjería de la provincia donde se vaya a desarrollar el trabajo."),
            ("Resolución de la autorización", "La Oficina de Extranjería resuelve en un plazo máximo de 3 meses."),
            ("Solicitud de visado", "El trabajador solicita el visado en el consulado español de su país."),
            ("Alta en la Seguridad Social y TIE", "El empresario da de alta al trabajador y este solicita su tarjeta.")
        ],
        "plazo": "De 2 a 5 meses en total"
    },
    {
        "filename": "residencia-trabajo-cuenta-propia.html",
        "category": "Residencias",
        "title": "Residencia y Trabajo por Cuenta Propia",
        "tagline": "Emprende en España. Si tienes un proyecto de negocio viable, esta es tu autorización.",
        "que_es": "Es la autorización que permite a un extranjero no comunitario residir en España para desarrollar una actividad económica por cuenta propia (autónomo o societaria). Debe acreditarse la viabilidad del proyecto empresarial y la inversión suficiente.",
        "quien": [
            "Extranjeros no comunitarios con un proyecto de negocio viable en España",
            "Personas con cualificación profesional suficiente o experiencia acreditada en la actividad",
            "Personas con inversión económica suficiente para el proyecto"
        ],
        "documentos": [
            "Pasaporte completo",
            "Plan de negocio detallado con proyección económica",
            "Acreditación de la cualificación profesional o experiencia",
            "Acreditación de la inversión prevista (extractos bancarios, préstamos)",
            "Certificado de antecedentes penales",
            "Documentación relativa al local o establecimiento (contrato de arrendamiento, licencias)"
        ],
        "pasos": [
            ("Elaborar plan de negocio", "Redactar un plan detallado que demuestre la viabilidad del proyecto."),
            ("Presentar solicitud en la Oficina de Extranjería", "O bien el propio interesado desde España (si está en situación legal) o a través del consulado."),
            ("Resolución de la autorización", "Se evalúa la viabilidad del proyecto y los requisitos personales."),
            ("Solicitar visado y viajar a España", "Si se solicita desde fuera, tramitar el visado consular."),
            ("Alta como autónomo y solicitud de TIE", "Darse de alta en Hacienda y Seguridad Social y tramitar la tarjeta.")
        ],
        "plazo": "De 2 a 5 meses en total"
    },
    {
        "filename": "residencia-no-lucrativa.html",
        "category": "Residencias",
        "title": "Residencia No Lucrativa",
        "tagline": "Vive en España sin trabajar, demostrando que dispones de medios económicos suficientes.",
        "que_es": "Es la autorización de residencia temporal que permite vivir en España sin realizar actividad laboral ni profesional. Está pensada para personas con ingresos o patrimonio propios suficientes: jubilados, rentistas o personas con ingresos pasivos.",
        "quien": [
            "Extranjeros no comunitarios que no vayan a trabajar en España",
            "Personas con medios económicos suficientes (aprox. 400% del IPREM, unos 2.400€/mes)",
            "Personas con seguro médico privado completo",
            "Personas sin antecedentes penales"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Certificado de antecedentes penales",
            "Certificado médico",
            "Acreditación de medios económicos (extractos bancarios, pensiones, rentas, patrimonio)",
            "Seguro médico privado con entidad autorizada en España"
        ],
        "pasos": [
            ("Reunir documentación económica", "Preparar pruebas de solvencia económica suficiente."),
            ("Solicitar el visado en el Consulado", "Presentar la solicitud con toda la documentación requerida."),
            ("Resolución y concesión del visado", "El consulado evalúa la solicitud y emite el visado."),
            ("Viajar a España", "Entrar en España dentro del plazo de validez del visado."),
            ("Solicitar la TIE", "En el mes siguiente a la entrada, tramitar la tarjeta de residencia.")
        ],
        "plazo": "De 1 a 3 meses para el visado"
    },
    {
        "filename": "residencia-arraigo-social.html",
        "category": "Residencias",
        "title": "Residencia por Arraigo Social",
        "tagline": "Si llevas al menos 3 años en España y tienes vínculos sociales, puedes regularizar tu situación.",
        "que_es": "Es una de las formas más comunes de regularización. Permite obtener una autorización de residencia temporal a extranjeros que se encuentran en España de forma irregular pero que demuestran una permanencia continuada de al menos 3 años y vínculos con la sociedad española (familiares con residencia legal o un informe de inserción social).",
        "quien": [
            "Extranjeros que acrediten permanencia continuada en España durante al menos 3 años",
            "Que no tengan antecedentes penales en España ni en su país de origen",
            "Que cuenten con un contrato de trabajo de al menos 1 año, o bien vínculos familiares con residente legal y un informe de inserción social"
        ],
        "documentos": [
            "Pasaporte completo",
            "Acreditación de permanencia de 3 años (empadronamiento, documentación sanitaria, envíos de dinero, etc.)",
            "Certificado de antecedentes penales del país de origen",
            "Contrato de trabajo de al menos 1 año de duración, o bien:",
            "Informe de inserción social emitido por los servicios sociales del ayuntamiento o comunidad autónoma",
            "Documentación que acredite vínculos familiares (si aplica)"
        ],
        "pasos": [
            ("Reunir pruebas de permanencia", "Recopilar toda la documentación que demuestre los 3 años en España."),
            ("Obtener contrato de trabajo o informe de inserción social", "Conseguir un contrato de al menos 1 año o el informe de servicios sociales."),
            ("Presentar solicitud en la Oficina de Extranjería", "Solicitar la autorización de residencia temporal por arraigo social."),
            ("Resolución", "La Oficina de Extranjería evalúa el expediente y resuelve."),
            ("Alta en la Seguridad Social y TIE", "Si se concede, darse de alta y tramitar la tarjeta.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "residencia-arraigo-segunda-oportunidad.html",
        "category": "Residencias",
        "title": "Residencia por Arraigo de Segunda Oportunidad",
        "tagline": "Si tuviste residencia legal y la perdiste, esta vía te permite recuperar tu situación.",
        "que_es": "Introducido por el Reglamento de Extranjería de 2022, el arraigo de segunda oportunidad permite regularizar su situación a quienes tuvieron una autorización de residencia en España y no pudieron renovarla. Es una segunda oportunidad para quienes cayeron en irregularidad sobrevenida por no cumplir requisitos de renovación.",
        "quien": [
            "Extranjeros que hayan sido titulares de una autorización de residencia previa en España",
            "Que la autorización se haya extinguido por no haber sido renovada",
            "Que se encuentren en España en el momento de la solicitud",
            "Que carezcan de antecedentes penales"
        ],
        "documentos": [
            "Pasaporte completo",
            "Documentación que acredite la titularidad anterior de una autorización de residencia",
            "Certificado de antecedentes penales del país de origen",
            "Certificado de empadronamiento",
            "Contrato de trabajo o medios económicos suficientes"
        ],
        "pasos": [
            ("Acreditar la autorización anterior", "Reunir documentación que demuestre que tuviste residencia legal en España."),
            ("Obtener contrato de trabajo", "Conseguir un contrato o acreditar medios económicos."),
            ("Presentar solicitud en la Oficina de Extranjería", "Solicitar el arraigo de segunda oportunidad."),
            ("Resolución", "La administración evalúa el expediente."),
            ("Obtener TIE", "Si se concede, tramitar la tarjeta de residencia y trabajo.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "residencia-arraigo-socioformativo.html",
        "category": "Residencias",
        "title": "Residencia por Arraigo Socioformativo",
        "tagline": "Combina formación oficial con arraigo: estudia y regulariza tu situación al mismo tiempo.",
        "que_es": "Es una modalidad de arraigo introducida en 2022 que permite obtener una autorización de residencia a extranjeros que llevan al menos 2 años en España y se comprometen a realizar una formación reglada para la obtención de un certificado o título oficial. Combina integración social con formación profesional.",
        "quien": [
            "Extranjeros con permanencia continuada en España de al menos 2 años",
            "Que se comprometan a realizar formación para la obtención de un certificado de profesionalidad o titulación oficial",
            "Sin antecedentes penales en España ni en su país de origen"
        ],
        "documentos": [
            "Pasaporte completo",
            "Acreditación de permanencia de al menos 2 años en España",
            "Matrícula o compromiso de admisión en el centro formativo para formación reglada",
            "Certificado de antecedentes penales del país de origen",
            "Certificado de empadronamiento"
        ],
        "pasos": [
            ("Acreditar 2 años de permanencia", "Reunir documentación que demuestre la estancia continuada."),
            ("Matricularse en formación oficial", "Inscribirse en un curso que conduzca a un certificado de profesionalidad o título oficial."),
            ("Presentar solicitud en la Oficina de Extranjería", "Solicitar la autorización de residencia por arraigo socioformativo."),
            ("Resolución", "La administración evalúa el expediente."),
            ("Obtener TIE y completar la formación", "Si se concede, se obtiene residencia por 1 año renovable mientras se mantiene la formación.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "residencia-arraigo-sociolaboral.html",
        "category": "Residencias",
        "title": "Residencia por Arraigo Sociolaboral",
        "tagline": "Si llevas 2 años en España y puedes demostrar experiencia laboral, esta vía es para ti.",
        "que_es": "Es una modalidad de arraigo que permite obtener residencia a extranjeros que llevan al menos 2 años de permanencia continuada en España y pueden acreditar una relación laboral de al menos 6 meses (dentro de los 2 años previos). Es una alternativa al arraigo social con menor tiempo de permanencia pero requiere experiencia laboral demostrable.",
        "quien": [
            "Extranjeros con permanencia continuada en España de al menos 2 años",
            "Que puedan acreditar una actividad laboral de al menos 6 meses (mediante sentencia judicial, acta de la Inspección de Trabajo o resolución administrativa)",
            "Sin antecedentes penales"
        ],
        "documentos": [
            "Pasaporte completo",
            "Acreditación de permanencia de al menos 2 años en España",
            "Sentencia judicial, acta de Inspección de Trabajo o resolución administrativa que acredite la actividad laboral de al menos 6 meses",
            "Certificado de antecedentes penales del país de origen",
            "Certificado de empadronamiento"
        ],
        "pasos": [
            ("Acreditar permanencia y experiencia laboral", "Reunir pruebas de estancia de 2 años y la resolución/sentencia que acredite el trabajo."),
            ("Presentar solicitud en la Oficina de Extranjería", "Solicitar la autorización de residencia por arraigo sociolaboral."),
            ("Resolución de la solicitud", "La administración evalúa la documentación."),
            ("Obtener TIE", "Si se concede, tramitar la tarjeta de residencia y trabajo.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "residencia-altamente-cualificado.html",
        "category": "Residencias",
        "title": "Residencia Profesional Altamente Cualificado",
        "tagline": "Si eres un profesional con alta cualificación, España facilita tu residencia con un trámite acelerado.",
        "que_es": "Es la autorización de residencia y trabajo dirigida a profesionales altamente cualificados que cuenten con titulación universitaria superior o experiencia profesional equivalente. Se tramita a través de la Unidad de Grandes Empresas y Colectivos Estratégicos (UGE-CE) con plazos más cortos que la autorización ordinaria.",
        "quien": [
            "Profesionales con titulación universitaria superior o experiencia profesional acreditada de al menos 5 años en un nivel comparable",
            "Que tengan una oferta de empleo con salario al menos 1,5 veces superior al salario medio bruto anual en España",
            "Empresas que cumplan los requisitos para contratar a un trabajador altamente cualificado"
        ],
        "documentos": [
            "Pasaporte completo",
            "Título universitario o acreditación de experiencia profesional equivalente",
            "Contrato de trabajo con salario mínimo requerido",
            "Documentación de la empresa (escrituras, poderes, CIF, TC1/TC2)",
            "Certificado de antecedentes penales"
        ],
        "pasos": [
            ("La empresa presenta la solicitud", "Ante la UGE-CE (Unidad de Grandes Empresas y Colectivos Estratégicos)."),
            ("Resolución acelerada", "La UGE-CE resuelve en un plazo reducido de 20 días hábiles."),
            ("Solicitar visado en el Consulado", "El trabajador tramita el visado con la autorización concedida."),
            ("Alta en Seguridad Social y TIE", "Incorporación al trabajo y tramitación de la tarjeta de residencia.")
        ],
        "plazo": "De 1 a 3 meses en total"
    },
    {
        "filename": "residencia-nomada-digital.html",
        "category": "Residencias",
        "title": "Residencia Nómada Digital",
        "tagline": "Trabaja en remoto desde España. La nueva autorización para profesionales que teletrabajan para empresas extranjeras.",
        "que_es": "Introducida por la Ley de Startups (Ley 28/2022), esta autorización permite a trabajadores por cuenta ajena o autónomos de empresas extranjeras residir en España mientras teletrabajan. Es ideal para profesionales digitales que quieren disfrutar de la calidad de vida española sin perder su empleo internacional.",
        "quien": [
            "Profesionales que realicen una actividad laboral o profesional a distancia para empresas situadas fuera de España",
            "Que puedan acreditar una relación laboral o profesional de al menos 1 año con la empresa extranjera, o que la empresa tenga al menos 1 año de antigüedad",
            "Que acrediten una titulación universitaria o de formación profesional de escuelas de prestigio"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Contrato de trabajo o certificación de la relación profesional con la empresa extranjera",
            "Acreditación de la antigüedad de la empresa (al menos 1 año) o de la relación laboral (al menos 1 año)",
            "Titulación universitaria o de formación profesional",
            "Certificado de antecedentes penales",
            "Seguro médico público o privado"
        ],
        "pasos": [
            ("Verificar requisitos", "Comprobar que cumples los requisitos de relación laboral con empresa extranjera."),
            ("Solicitar visado o autorización", "Si estás fuera de España, solicitar visado; si ya estás en España legalmente, solicitar la autorización directamente."),
            ("Resolución", "La UGE-CE resuelve en un plazo de 20 días hábiles."),
            ("Obtener TIE", "Tramitar la tarjeta de residencia con validez de hasta 3 años.")
        ],
        "plazo": "De 20 días hábiles a 3 meses"
    },
    {
        "filename": "residencia-ciudadano-ue.html",
        "category": "Residencias",
        "title": "Residencia de Ciudadano de la Unión",
        "tagline": "Si eres ciudadano europeo, tienes derecho a residir en España. Solo necesitas inscribirte en el registro.",
        "que_es": "Los ciudadanos de la Unión Europea, del Espacio Económico Europeo y de Suiza tienen derecho a residir libremente en España. Para estancias superiores a 3 meses, deben inscribirse en el Registro Central de Extranjeros y obtener el Certificado de Registro de Ciudadano de la UE (el famoso NIE verde).",
        "quien": [
            "Ciudadanos de cualquier país de la UE, EEE (Noruega, Islandia, Liechtenstein) o Suiza",
            "Que cumplan alguna de estas condiciones: ser trabajador por cuenta ajena o propia en España, tener recursos suficientes y seguro médico, o ser estudiante con seguro y recursos"
        ],
        "documentos": [
            "Pasaporte o documento de identidad del país de origen en vigor",
            "Justificante de empleo (contrato, alta en la Seguridad Social), o acreditación de recursos económicos y seguro médico, o matrícula de estudios",
            "Formulario EX-18",
            "Justificante del pago de la tasa (modelo 790, código 012)"
        ],
        "pasos": [
            ("Obtener cita previa", "Solicitar cita en la comisaría de policía o en la Oficina de Extranjería."),
            ("Acudir con la documentación", "Presentar el formulario y la documentación acreditativa."),
            ("Obtener el certificado de registro (NIE verde)", "En el mismo acto se expide el certificado con tu NIE.")
        ],
        "plazo": "Inmediato o pocos días desde la solicitud"
    },
    {
        "filename": "residencia-larga-duracion.html",
        "category": "Residencias",
        "title": "Residencia de Larga Duración",
        "tagline": "Tras 5 años de residencia legal continuada, obtén una autorización permanente para vivir y trabajar sin límites.",
        "que_es": "Es la autorización que se concede a los extranjeros que han residido legalmente y de forma continuada en España durante al menos 5 años. Otorga el derecho a residir y trabajar en España indefinidamente, en las mismas condiciones que los españoles, y la tarjeta tiene una validez de 5 años renovable.",
        "quien": [
            "Extranjeros con residencia legal y continuada en España durante 5 años",
            "Que no se hayan ausentado del territorio español más de 6 meses consecutivos (ni más de 10 meses en total en los 5 años)",
            "Sin antecedentes penales"
        ],
        "documentos": [
            "Pasaporte completo en vigor",
            "Tarjeta de residencia vigente",
            "Certificado de antecedentes penales (si se solicita)",
            "Acreditación de la continuidad de la residencia (empadronamiento histórico, vida laboral)",
            "Formulario EX-11"
        ],
        "pasos": [
            ("Verificar el cumplimiento de los 5 años", "Comprobar que no se han superado los límites de ausencia."),
            ("Presentar solicitud", "En la Oficina de Extranjería con la documentación requerida."),
            ("Resolución", "La Oficina de Extranjería evalúa el expediente."),
            ("Obtener nueva TIE de larga duración", "Se expide la tarjeta con validez de 5 años renovable.")
        ],
        "plazo": "De 1 a 3 meses"
    },
    {
        "filename": "residencia-contrataciones-origen.html",
        "category": "Residencias",
        "title": "Residencia por Contrataciones en Origen",
        "tagline": "Si estás en tu país y una empresa española quiere contratarte, este es el procedimiento para venir a trabajar legalmente.",
        "que_es": "Es el procedimiento mediante el cual un empresario en España contrata a un trabajador extranjero que se encuentra en su país de origen. Se gestiona a través de la llamada gestión colectiva de contrataciones en origen o de forma individual. Es especialmente común en sectores como agricultura, hostelería y construcción.",
        "quien": [
            "Trabajadores extranjeros que se encuentren en su país de origen (no en España)",
            "Que cuenten con una oferta de empleo de un empresario en España",
            "Que no tengan antecedentes penales",
            "Que la situación nacional de empleo permita la contratación (o exista un convenio bilateral)"
        ],
        "documentos": [
            "Pasaporte del trabajador",
            "Oferta de empleo firmada por el empresario",
            "Documentación de la empresa (CIF, TC, escrituras)",
            "Certificado de antecedentes penales del trabajador",
            "Certificado médico"
        ],
        "pasos": [
            ("El empresario gestiona la autorización", "Presenta la solicitud ante la Oficina de Extranjería o a través de una gestión colectiva."),
            ("Resolución de la autorización", "La administración verifica los requisitos y concede la autorización."),
            ("El trabajador solicita el visado", "En el consulado español de su país con la autorización concedida."),
            ("Viaje a España y alta laboral", "El trabajador viaja, se da de alta en la Seguridad Social y empieza a trabajar."),
            ("Solicitud de TIE", "En el mes siguiente, tramitar la tarjeta de residencia.")
        ],
        "plazo": "De 2 a 5 meses en total"
    },

    # ── MODIFICACIONES (5) ──
    {
        "filename": "modificacion-estudios-a-trabajo.html",
        "category": "Modificaciones",
        "title": "De Estancia por Estudios a Residencia y Trabajo por Cuenta Ajena",
        "tagline": "Terminaste tus estudios en España y quieres quedarte a trabajar. Puedes cambiar tu estatus sin salir del país.",
        "que_es": "Es la modificación que permite a los extranjeros que se encuentran en España con un visado de estudiante pasar a una autorización de residencia y trabajo por cuenta ajena sin necesidad de regresar a su país. Se exige haber completado los estudios o haber superado al menos el primer curso.",
        "quien": [
            "Titulares de una autorización de estancia por estudios en vigor",
            "Que hayan superado con éxito los estudios o al menos el primer año",
            "Que cuenten con un contrato de trabajo de al menos 1 año"
        ],
        "documentos": [
            "Pasaporte completo en vigor",
            "Tarjeta de estudiante en vigor",
            "Certificado académico o título que acredite la superación de los estudios",
            "Contrato de trabajo de al menos 1 año de duración",
            "Documentación de la empresa (CIF, TC, escrituras)"
        ],
        "pasos": [
            ("Finalizar o aprobar los estudios", "Obtener el certificado académico que lo acredite."),
            ("Conseguir contrato de trabajo", "Que una empresa te ofrezca un contrato de al menos 1 año."),
            ("Presentar solicitud de modificación", "En la Oficina de Extranjería antes de que expire la estancia por estudios."),
            ("Resolución", "La administración evalúa si se cumplen los requisitos."),
            ("Obtener nueva TIE de residencia y trabajo", "Si se concede, tramitar la nueva tarjeta.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "modificacion-excepcionales-a-trabajo.html",
        "category": "Modificaciones",
        "title": "De Circunstancias Excepcionales a Residencia y Trabajo",
        "tagline": "Si obtuviste residencia por arraigo u otra circunstancia excepcional, puedes pasar a un permiso de trabajo ordinario.",
        "que_es": "Es la modificación que permite a los titulares de una autorización de residencia por circunstancias excepcionales (arraigo social, arraigo laboral, protección internacional, razones humanitarias, etc.) pasar a una autorización de residencia y trabajo por cuenta ajena ordinaria cuando cumplan los requisitos.",
        "quien": [
            "Titulares de una autorización de residencia por circunstancias excepcionales en vigor",
            "Que cuenten con un contrato de trabajo",
            "Que cumplan los requisitos generales para la autorización de trabajo por cuenta ajena"
        ],
        "documentos": [
            "Pasaporte completo",
            "Tarjeta de residencia vigente (por circunstancias excepcionales)",
            "Contrato de trabajo",
            "Documentación de la empresa",
            "Vida laboral actualizada (si ya has trabajado previamente)"
        ],
        "pasos": [
            ("Conseguir contrato de trabajo", "Que un empleador te ofrezca un contrato de trabajo."),
            ("Presentar solicitud de modificación", "Ante la Oficina de Extranjería antes de que expire tu autorización actual."),
            ("Resolución", "La administración evalúa la documentación."),
            ("Obtener nueva TIE", "Si se concede, tramitar la nueva tarjeta de residencia y trabajo.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "modificacion-comunitario-a-trabajo.html",
        "category": "Modificaciones",
        "title": "Del Régimen Comunitario a Residencia por Cuenta Ajena",
        "tagline": "Si perdiste tu tarjeta de familiar de la UE por divorcio o nulidad, puedes mantener tu residencia en España.",
        "que_es": "Cuando un extranjero que tenía tarjeta de familiar de ciudadano de la UE pierde ese derecho por nulidad del matrimonio, divorcio o cancelación de la pareja de hecho, puede solicitar una modificación a una autorización de residencia y trabajo por cuenta ajena del régimen general. Esto evita caer en situación irregular.",
        "quien": [
            "Titulares de tarjeta de familiar de ciudadano de la UE cuyo vínculo matrimonial o de pareja se haya disuelto",
            "Que hayan residido legalmente en España con dicha tarjeta al menos 1 año",
            "Que cuenten con un contrato de trabajo o acrediten medios económicos"
        ],
        "documentos": [
            "Pasaporte completo",
            "Tarjeta de familiar de ciudadano de la UE (aunque esté caducada si se solicita en plazo)",
            "Sentencia de divorcio, nulidad o certificado de cancelación de pareja de hecho",
            "Contrato de trabajo o acreditación de medios económicos",
            "Certificado de empadronamiento"
        ],
        "pasos": [
            ("Obtener sentencia o certificado de disolución", "Reunir la documentación que acredite la ruptura del vínculo."),
            ("Presentar solicitud de modificación", "Ante la Oficina de Extranjería en el plazo establecido."),
            ("Resolución", "La administración evalúa si se cumplen los requisitos."),
            ("Obtener nueva TIE del régimen general", "Si se concede, tramitar la tarjeta de residencia y trabajo.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "modificacion-residencia-a-trabajo-ajena.html",
        "category": "Modificaciones",
        "title": "De Residencia a Residencia y Trabajo por Cuenta Ajena",
        "tagline": "Si tienes residencia sin permiso de trabajo, puedes añadir la autorización laboral a tu tarjeta.",
        "que_es": "Es la modificación que permite a quienes tienen una autorización de residencia sin permiso de trabajo (por ejemplo, residencia no lucrativa o residencia por reagrupación sin autorización de trabajo) obtener una autorización que les habilite para trabajar por cuenta ajena.",
        "quien": [
            "Titulares de una autorización de residencia sin permiso de trabajo (no lucrativa, reagrupación familiar sin trabajo, etc.)",
            "Que cuenten con un contrato de trabajo",
            "Que la autorización de residencia esté en vigor"
        ],
        "documentos": [
            "Pasaporte completo",
            "Tarjeta de residencia vigente",
            "Contrato de trabajo",
            "Documentación de la empresa (CIF, escrituras, TC, última declaración de IRPF o Sociedades)"
        ],
        "pasos": [
            ("Conseguir una oferta de empleo", "Que un empleador te ofrezca un contrato de trabajo."),
            ("Presentar solicitud de modificación", "Ante la Oficina de Extranjería."),
            ("Resolución", "La administración comprueba los requisitos."),
            ("Obtener nueva TIE con autorización de trabajo", "Si se aprueba, tramitar la nueva tarjeta.")
        ],
        "plazo": "De 2 a 4 meses"
    },
    {
        "filename": "modificacion-residencia-a-trabajo-propia.html",
        "category": "Modificaciones",
        "title": "De Residencia a Residencia y Trabajo por Cuenta Propia",
        "tagline": "Si ya resides en España y quieres emprender como autónomo, modifica tu autorización sin salir del país.",
        "que_es": "Es la modificación que permite a quienes tienen una autorización de residencia sin permiso de trabajo (o con trabajo por cuenta ajena) pasar a una autorización de residencia y trabajo por cuenta propia para desarrollar una actividad empresarial o profesional como autónomo.",
        "quien": [
            "Titulares de una autorización de residencia en vigor",
            "Que presenten un proyecto de negocio viable",
            "Que acrediten cualificación profesional y medios económicos para el emprendimiento"
        ],
        "documentos": [
            "Pasaporte completo",
            "Tarjeta de residencia vigente",
            "Plan de negocio detallado con proyección económica",
            "Acreditación de cualificación profesional o experiencia",
            "Acreditación de la inversión prevista",
            "Documentación del local o establecimiento (si aplica)"
        ],
        "pasos": [
            ("Elaborar plan de negocio", "Redactar un plan que demuestre la viabilidad de tu proyecto."),
            ("Presentar solicitud de modificación", "Ante la Oficina de Extranjería con toda la documentación."),
            ("Resolución", "La administración evalúa la viabilidad del proyecto y los requisitos."),
            ("Darse de alta como autónomo", "Si se concede, alta en Hacienda y Seguridad Social."),
            ("Obtener nueva TIE", "Tramitar la tarjeta de residencia y trabajo por cuenta propia.")
        ],
        "plazo": "De 2 a 4 meses"
    },

    # ── RENOVACIONES (5) ──
    {
        "filename": "renovacion-no-lucrativa.html",
        "category": "Renovaciones",
        "title": "Renovación de Residencia No Lucrativa",
        "tagline": "Renueva tu residencia no lucrativa y sigue disfrutando de España sin preocupaciones.",
        "que_es": "La autorización de residencia no lucrativa tiene una validez inicial de 1 año y puede renovarse por periodos sucesivos de 2 años. Para renovar, debes demostrar que sigues cumpliendo los requisitos: medios económicos suficientes, seguro médico y que no has trabajado en España.",
        "quien": [
            "Titulares de una autorización de residencia no lucrativa en vigor o dentro del plazo de renovación",
            "Que sigan contando con medios económicos suficientes",
            "Que mantengan seguro médico privado",
            "Que no hayan trabajado durante la vigencia de la autorización"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Tarjeta de residencia actual",
            "Acreditación de medios económicos actualizados",
            "Seguro médico en vigor",
            "Certificado de empadronamiento",
            "Tasa de renovación (modelo 790, código 052)"
        ],
        "pasos": [
            ("Solicitar renovación en plazo", "Presentar la solicitud en los 60 días previos a la caducidad (o 90 días posteriores con recargo)."),
            ("Acreditar que sigues cumpliendo requisitos", "Presentar documentación económica y seguro actualizados."),
            ("Resolución", "La Oficina de Extranjería evalúa la solicitud."),
            ("Obtener nueva TIE", "Si se concede, tramitar la nueva tarjeta con validez de 2 años.")
        ],
        "plazo": "De 1 a 3 meses"
    },
    {
        "filename": "renovacion-trabajo.html",
        "category": "Renovaciones",
        "title": "Renovación de Residencia por Trabajo Cuenta Ajena / Propia",
        "tagline": "No dejes que tu autorización caduque. Renueva a tiempo y sigue trabajando legalmente en España.",
        "que_es": "La renovación de la autorización de residencia y trabajo (tanto por cuenta ajena como propia) se realiza cuando está próxima a caducar la tarjeta vigente. Se evalúa que se sigan cumpliendo los requisitos: contrato de trabajo en vigor o actividad autónoma activa, y medios económicos suficientes.",
        "quien": [
            "Titulares de autorización de residencia y trabajo (cuenta ajena o propia) en vigor o en plazo de renovación",
            "Que mantengan la actividad laboral o profesional que motivó la autorización",
            "Que no tengan deudas con la Seguridad Social ni con Hacienda"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Tarjeta de residencia actual",
            "Contrato de trabajo vigente o certificado de actividad autónoma",
            "Vida laboral actualizada",
            "Última declaración de IRPF o certificado negativo de Hacienda",
            "Certificado de estar al corriente con la Seguridad Social",
            "Tasa de renovación (modelo 790, código 052)"
        ],
        "pasos": [
            ("Solicitar renovación en plazo", "60 días antes de la caducidad o hasta 90 días después (con recargo)."),
            ("Acreditar continuidad laboral", "Presentar contrato vigente, vida laboral y documentación fiscal."),
            ("Resolución", "La Oficina de Extranjería evalúa la solicitud."),
            ("Obtener nueva TIE", "Si se concede, tramitar la nueva tarjeta con validez de 2 años.")
        ],
        "plazo": "De 1 a 3 meses"
    },
    {
        "filename": "renovacion-altamente-cualificado.html",
        "category": "Renovaciones",
        "title": "Renovación de Residencia Altamente Cualificado",
        "tagline": "Renueva tu Tarjeta Azul UE y sigue desarrollando tu carrera profesional en España.",
        "que_es": "La renovación de la autorización de residencia para profesionales altamente cualificados (Tarjeta Azul UE) se tramita ante la UGE-CE. Debe acreditarse que se mantiene la relación laboral cualificada con las condiciones exigidas.",
        "quien": [
            "Titulares de autorización de residencia de profesional altamente cualificado",
            "Que mantengan la relación laboral cualificada con salario mínimo requerido",
            "Que la empresa siga cumpliendo los requisitos"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Tarjeta de residencia actual",
            "Contrato de trabajo vigente con salario requerido",
            "Vida laboral actualizada",
            "Documentación actualizada de la empresa",
            "Tasa de renovación"
        ],
        "pasos": [
            ("Verificar que se mantienen las condiciones", "Comprobar que el salario y puesto siguen cumpliendo los requisitos."),
            ("Presentar solicitud ante la UGE-CE", "En el plazo de renovación establecido."),
            ("Resolución acelerada", "La UGE-CE resuelve en un plazo reducido."),
            ("Obtener nueva TIE", "Tramitar la nueva tarjeta de residencia.")
        ],
        "plazo": "De 20 días hábiles a 2 meses"
    },
    {
        "filename": "renovacion-investigacion.html",
        "category": "Renovaciones",
        "title": "Renovación de Residencia para Investigación",
        "tagline": "Continúa tu proyecto de investigación en España renovando tu autorización de forma ágil.",
        "que_es": "Los investigadores extranjeros que han sido acogidos por un organismo de investigación en España pueden renovar su autorización de residencia mientras continúe el proyecto de investigación o se inicie uno nuevo. El procedimiento es similar al de la concesión inicial.",
        "quien": [
            "Titulares de autorización de residencia para investigación",
            "Que mantengan el convenio de acogida con un organismo de investigación en España o cuenten con uno nuevo",
            "Que el organismo de investigación siga estando acreditado"
        ],
        "documentos": [
            "Pasaporte en vigor",
            "Tarjeta de residencia actual",
            "Convenio de acogida vigente con el organismo de investigación",
            "Acreditación del organismo de investigación",
            "Acreditación de medios económicos y seguro médico",
            "Tasa de renovación"
        ],
        "pasos": [
            ("Asegurar la continuidad del convenio de acogida", "Renovar o firmar un nuevo convenio con el organismo de investigación."),
            ("Presentar solicitud de renovación", "Ante la Oficina de Extranjería o la UGE-CE."),
            ("Resolución", "La administración comprueba los requisitos."),
            ("Obtener nueva TIE", "Tramitar la nueva tarjeta de residencia.")
        ],
        "plazo": "De 1 a 3 meses"
    },
    {
        "filename": "renovacion-agrupacion-familiar.html",
        "category": "Renovaciones",
        "title": "Renovación de Residencia por Agrupación Familiar",
        "tagline": "Renueva la residencia que obtuviste por reagrupación familiar y sigue junto a tu familia en España.",
        "que_es": "La autorización de residencia obtenida por reagrupación familiar debe renovarse al caducar. En la renovación se comprueba que se mantienen las circunstancias que dieron lugar a la reagrupación: que el reagrupante siga teniendo residencia legal y medios, y que persista el vínculo familiar.",
        "quien": [
            "Titulares de autorización de residencia obtenida por reagrupación familiar",
            "Que el reagrupante mantenga residencia legal en España",
            "Que persista el vínculo familiar que motivó la reagrupación",
            "Que el reagrupante acredite medios económicos y vivienda adecuada"
        ],
        "documentos": [
            "Pasaporte en vigor del familiar reagrupado",
            "Tarjeta de residencia actual",
            "Tarjeta de residencia del reagrupante en vigor",
            "Acreditación de medios económicos del reagrupante (nóminas, IRPF, vida laboral)",
            "Certificado de convivencia o empadronamiento conjunto",
            "Tasa de renovación"
        ],
        "pasos": [
            ("Solicitar renovación en plazo", "60 días antes de la caducidad o hasta 90 días después."),
            ("Acreditar que se mantiene el vínculo", "Presentar certificado de convivencia y documentación del reagrupante."),
            ("Resolución", "La Oficina de Extranjería evalúa la solicitud."),
            ("Obtener nueva TIE", "Si se concede, tramitar la nueva tarjeta con validez de 2 años.")
        ],
        "plazo": "De 1 a 3 meses"
    },
]


# ══════════════════════════════════════════════════════════════
#  BUILD: "Otras Especialidades" pages
# ══════════════════════════════════════════════════════════════
icons = ["ri-check-double-line", "ri-scales-3-line", "ri-shield-check-line", "ri-file-paper-2-line", "ri-user-star-line", "ri-building-line"]

for page in pages_data:
    # Services HTML
    services_html = ""
    for idx, (svc_title, svc_desc) in enumerate(page["services"]):
        icon = icons[idx % len(icons)]
        services_html += f"<li><i class='{icon}'></i><div><strong style='display:block; font-size:1.1rem; margin-bottom:0.2rem; color:var(--text-main);'>{svc_title}</strong><span style='color:var(--text-dim);'>{svc_desc}</span></div></li>\n"

    # Stats HTML
    stats_html = ""
    for val, prefix, suffix, label in page.get("stats", []):
        stats_html += f"""<div class="stat-card">
            <div class="stat-number"><span class="stat-counter" data-target="{val}" data-prefix="{prefix}" data-suffix="{suffix}">{prefix}0{suffix}</span></div>
            <div class="stat-label">{label}</div>
        </div>\n"""

    # Process Timeline HTML
    steps_html = ""
    for idx, (step_title, step_desc) in enumerate(page.get("steps", []), 1):
        steps_html += f"""<div class="timeline-item" data-step="{idx}">
            <h4>{step_title}</h4>
            <p>{step_desc}</p>
        </div>\n"""

    # Highlights HTML
    highlights_html = ""
    for hi_icon, hi_title, hi_desc in page.get("highlights", []):
        highlights_html += f"""<div class="highlight-card">
            <i class="{hi_icon}"></i>
            <h4>{hi_title}</h4>
            <p>{hi_desc}</p>
        </div>\n"""

    # FAQ HTML
    faq_html = ""
    for faq_q, faq_a in page.get("faqs", []):
        faq_html += f"""<div class="faq-item">
            <button class="faq-question">{faq_q}<i class="ri-arrow-down-s-line"></i></button>
            <div class="faq-answer"><p>{faq_a}</p></div>
        </div>\n"""

    final_html = template.format(
        title=page["title"],
        icon=page["icon"],
        desc=page["desc"],
        services_html=services_html,
        stats_html=stats_html,
        process_title=page.get("process_title", "Nuestro proceso de trabajo"),
        steps_html=steps_html,
        highlights_html=highlights_html,
        faq_html=faq_html,
        header=header,
        footer=footer
    )

    with open(page["filename"], "w", encoding="utf-8") as f:
        f.write(final_html)


# ══════════════════════════════════════════════════════════════
#  BUILD: Extranjería individual pages
# ══════════════════════════════════════════════════════════════
for page in extranjeria_data:
    requisitos_html = ""
    for req in page["quien"]:
        requisitos_html += f'<li><i class="ri-checkbox-circle-line"></i> {req}</li>\n'

    documentos_html = ""
    for doc in page["documentos"]:
        documentos_html += f'<li><i class="ri-file-text-line"></i> {doc}</li>\n'

    pasos_html = ""
    for idx, (paso_title, paso_desc) in enumerate(page["pasos"], 1):
        pasos_html += f"""<div class="step-item">
            <div class="step-num">{idx}</div>
            <div class="step-text"><h4>{paso_title}</h4><p>{paso_desc}</p></div>
        </div>\n"""

    final_html = extranjeria_template.format(
        title=page["title"],
        category=page["category"],
        tagline=page["tagline"],
        que_es=page["que_es"],
        requisitos_html=requisitos_html,
        documentos_html=documentos_html,
        pasos_html=pasos_html,
        plazo=page["plazo"],
        header=header,
        footer=footer
    )

    with open(page["filename"], "w", encoding="utf-8") as f:
        f.write(final_html)

print(f"Built {len(pages_data)} specialty pages + {len(extranjeria_data)} extranjería pages successfully.")
