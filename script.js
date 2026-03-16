/**
 * script.js - Behaviors for Luxury Law UI
 */

document.addEventListener('DOMContentLoaded', () => {

    /* --- Scroll Reveals via IntersectionObserver --- */
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-down');

    // Initial trigger for hero content
    setTimeout(() => {
        document.querySelector('.header').classList.add('active-reveal');
    }, 100);

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active-reveal');
                // Number Counter logic attached to reveal
                if (entry.target.classList.contains('trust-flex') && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    runCounters();
                }
                observer.unobserve(entry.target);
            }
        });
    }, { rootMargin: "0px 0px -100px 0px" });

    revealElements.forEach(el => revealObserver.observe(el));


    /* --- Number Counters --- */
    function runCounters() {
        const counters = document.querySelectorAll('.counter');
        const speed = 200; // The lower the slower
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.parentElement.getAttribute('data-val');
                const count = +counter.innerText;
                const inc = target / speed;
                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 10);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        });
    }


    /* --- Header Scroll Effect via GSAP --- */
    const header = document.querySelector('.header');

    let lastScrollY = 0;
    let headerTicking = false;
    window.addEventListener('scroll', () => {
        lastScrollY = window.scrollY;
        if (!headerTicking) {
            requestAnimationFrame(() => {
                if (lastScrollY > 50) {
                    if (!header.classList.contains('scrolled')) {
                        header.classList.add('scrolled');
                        if (typeof gsap !== 'undefined') {
                            gsap.fromTo(header,
                                { backgroundColor: '#3d5265', backdropFilter: 'blur(0px)' },
                                {
                                    backgroundColor: 'transparent',
                                    duration: 0.5,
                                    ease: "power2.out"
                                }
                            );
                        }
                    }
                } else {
                    if (header.classList.contains('scrolled')) {
                        header.classList.remove('scrolled');
                        if (typeof gsap !== 'undefined') {
                            gsap.fromTo(header,
                                { backgroundColor: 'rgba(61, 82, 101, 0.82)' },
                                {
                                    backgroundColor: '#3d5265',
                                    duration: 0.5,
                                    ease: "power2.out"
                                }
                            );
                        }
                    }
                }
                headerTicking = false;
            });
            headerTicking = true;
        }
    }, { passive: true });


    /* --- Alert Bar Close --- */
    const alertBar = document.getElementById('top-alert');
    const closeAlert = document.getElementById('close-alert');
    if (alertBar && closeAlert) {
        closeAlert.addEventListener('click', () => {
            alertBar.style.display = 'none';
        });
    }


    /* --- Applet Form (Smart Funnel) Logic --- */
    const pBar = document.getElementById('applet-progress');
    const pIndic = document.getElementById('step-indicator');

    // Track answers across all steps
    const funnelAnswers = {};

    // Step order for progress bar (logical steps 1 through 3)
    const TOTAL_LOGICAL_STEPS = 3;
    // Current logical step number (1 = who, 2 = situation, 3 = conditional, result/form = hidden)
    let logicalStep = 1;

    function getStepEl(stepId) {
        return document.querySelector(`.applet-step[data-step="${stepId}"]`);
    }

    // Attach to window so onclick in HTML works
    window.showStep = function (stepId) {
        // Hide all steps
        document.querySelectorAll('.applet-step').forEach(s => s.classList.remove('active'));
        // Show target
        const target = getStepEl(stepId);
        if (target) target.classList.add('active');

        // Special: If entering results step, generate them
        if (stepId === '4') {
            generateResults();
        }

        // Update logical step counter for progress
        // Steps 4, 5, 6 (result, form, success) complete the bar and hide the step indicator
        const logicalMap = { '1': 1, '2': 2, '3a': 3, '3b': 3, '3c': 3, '3d': 3, '4': null, '5': null, '6': null };
        const mapped = logicalMap[String(stepId)];
        if (mapped !== undefined && mapped !== null) {
            logicalStep = mapped;
            const pct = (logicalStep / TOTAL_LOGICAL_STEPS) * 100;
            if (pBar) pBar.style.width = pct + '%';
            if (pIndic) {
                pIndic.innerText = `Paso ${logicalStep} de ${TOTAL_LOGICAL_STEPS}`;
                pIndic.style.opacity = '1';
            }
        } else {
            // Result / form / success: full bar, hide step label
            if (pBar) pBar.style.width = '100%';
            if (pIndic) pIndic.style.opacity = '0';
        }

        // Update sidebar step highlights
        // Sidebar steps: sidebar-1=¿Para quién?, sidebar-2=Situación, sidebar-3=Objetivo, sidebar-4=Resultados
        const sidebarMap = { '1': 1, '2': 2, '3a': 3, '3b': 3, '3c': 3, '3d': 3, '4': 4, '5': 4, '6': 4 };
        const activeSidebar = sidebarMap[String(stepId)] || 1;
        for (let i = 1; i <= 4; i++) {
            const el = document.getElementById(`sidebar-${i}`);
            if (!el) continue;
            el.classList.remove('active-sidebar', 'done-sidebar');
            if (i < activeSidebar) {
                el.classList.add('done-sidebar');
            } else if (i === activeSidebar) {
                el.classList.add('active-sidebar');
            }
        }

        // Scroll right panel to top
        const evalRight = document.querySelector('.eval-right');
        if (evalRight) evalRight.scrollTop = 0;
    }

    // Handle option button clicks (data-goto)
    document.querySelectorAll('.applet-opt').forEach(opt => {
        opt.addEventListener('click', () => {
            const answer = opt.getAttribute('data-answer');
            const gotoStep = opt.getAttribute('data-goto');
            // Determine which question this belongs to by current visible step
            const parentStep = opt.closest('.applet-step');
            if (parentStep) {
                const stepId = parentStep.getAttribute('data-step');
                funnelAnswers[stepId] = answer;
            }
            if (gotoStep) {
                showStep(gotoStep);
            }
        });
    });

    // Handle back buttons
    document.querySelectorAll('.step-back').forEach(btn => {
        btn.addEventListener('click', () => {
            const gotoStep = btn.getAttribute('data-goto');
            if (gotoStep) showStep(gotoStep);
        });
    });

    // Generate result cards based on answers
    function generateResults() {
        const sit = funnelAnswers['2']; // main situation
        const sub = funnelAnswers['3a'] || funnelAnswers['3b'] || funnelAnswers['3c'] || funnelAnswers['3d']; // conditional answer

        const results = {
            fuera: {
                trabajo: [
                    { icon: 'ri-briefcase-4-line', title: 'Visado de Trabajo y Residencia (Cuenta Ajena)', desc: 'La vía más directa si tienes una oferta laboral de empresa española. Nuestros abogados gestionan el expediente completo.' },
                    { icon: 'ri-file-list-3-line', title: 'Contratación en Origen', desc: 'Si tu contrato se firma en tu país de origen, podemos acelerar el proceso de visado en la embajada española.' },
                ],
                autonomo: [
                    { icon: 'ri-store-3-line', title: 'Visado de Cuenta Propia (Autónomo)', desc: 'Para emprendedores y trabajadores independientes que quieran establecerse en España.' },
                    { icon: 'ri-lightbulb-line', title: 'Visado Emprendedor / Startup', desc: 'Si tienes un proyecto innovador, existe una vía específica para su internacionalización.' },
                ],
                nomada: [
                    { icon: 'ri-global-line', title: 'Visa Nómada Digital', desc: 'Permiso de residencia para trabajadores remotos de empresas no españolas. Vigencia inicial de 1 año, renovable.' },
                ],
                familiar_eu: [
                    { icon: 'ri-team-line', title: 'Reagrupación Familiar', desc: 'Si tienes un familiar con residencia legal en España, puedes solicitar la reagrupación para vivir juntos.' },
                    { icon: 'ri-heart-2-line', title: 'Familiar de Ciudadano UE o Español', desc: 'Proceso simplificado con más derechos si el familiar tiene nacionalidad española o europea.' },
                ],
                estudiar: [
                    { icon: 'ri-graduation-cap-line', title: 'Visado de Estudios', desc: 'Para matriculados en universidades, escuelas de idiomas u otras instituciones autorizadas en España.' },
                ],
                default: [
                    { icon: 'ri-passport-line', title: 'Visado de Residencia No Lucrativa', desc: 'Para quienes disponen de medios económicos suficientes y no necesitan trabajar en España.' },
                ]
            },
            irregular: {
                menos2: [
                    { icon: 'ri-map-pin-user-line', title: 'Arraigo Socioformativo', desc: 'Con menos de 2 años es posible regularizarse combinando formación y arraigo. Te asesoramos sobre los requisitos.' },
                    { icon: 'ri-family-line', title: 'Vía Familiar (si aplica)', desc: 'Si tienes pareja o hijos con residencia legal, existe una vía de regularización por lazos familiares.' },
                ],
                '2a3': [
                    { icon: 'ri-community-line', title: 'Arraigo Social (2 años)', desc: 'Posible a partir de 2 años de estancia acreditada. Se requiere informe de inserción social del ayuntamiento.' },
                    { icon: 'ri-briefcase-line', title: 'Arraigo Sociolaboral', desc: 'Si tienes relación laboral o experiencia demostrable, esta vía puede complementar el arraigo social.' },
                ],
                mas3: [
                    { icon: 'ri-community-line', title: 'Arraigo Social (3 años)', desc: 'La vía más común de regularización. Con 3 años de estancia y arraigo social demostrable.' },
                    { icon: 'ri-briefcase-4-line', title: 'Arraigo Sociolaboral / Segunda Oportunidad', desc: 'Alternativas de regularización con diferentes requisitos. Analizamos cuál encaja mejor con tu caso.' },
                    { icon: 'ri-shield-star-line', title: 'Regularización Masiva 2025–2026', desc: 'Nueva ventana de regularización excepcional. Consulta si puedes acogerte a esta medida extraordinaria.' },
                ],
                default: [
                    { icon: 'ri-shield-star-line', title: 'Análisis de Situación de Regularización', desc: 'Existen distintas vías según tus circunstancias. Un abogado analizará tu caso y encontrará la mejor opción.' },
                ]
            },
            estudiante: {
                trabajar: [
                    { icon: 'ri-briefcase-4-line', title: 'Modificación a Residencia y Trabajo', desc: 'Puedes modificar tu permiso de estudiante a uno de trabajo si tienes una oferta laboral o llevas tiempo en España.' },
                    { icon: 'ri-store-3-line', title: 'Residencia por Cuenta Propia', desc: 'Si quieres emprender tras graduarte, esta es la vía para regularizar tu situación como autónomo.' },
                ],
                seguir_estudios: [
                    { icon: 'ri-award-line', title: 'Renovación de Visado de Estudios', desc: 'Si continúas tu formación académica, tramitamos la renovación de tu permiso de estancia por estudios.' },
                ],
                residencia_perm: [
                    { icon: 'ri-home-4-line', title: 'Residencia de Larga Duración', desc: 'Tras 5 años de residencia legal ininterrumpida (incluidos los de estudios), puedes optar a la larga duración.' },
                    { icon: 'ri-passport-line', title: 'Nacionalidad Española', desc: 'Estudiando el historial y tu situación, podemos analizar si ya cumples requisitos de nacionalidad.' },
                ],
                default: [
                    { icon: 'ri-compass-line', title: 'Análisis de Situación Post-Estudios', desc: 'Evaluamos todas las opciones disponibles según tu situación académica y personal.' },
                ]
            },
            residente: {
                renovar: [
                    { icon: 'ri-refresh-line', title: 'Renovación de Permiso de Residencia', desc: 'Gestionamos la renovación de tu permiso actual, evitando errores que puedan causar demoras o denegaciones.' },
                ],
                larga_duracion: [
                    { icon: 'ri-vip-crown-line', title: 'Residencia de Larga Duración (UE)', desc: 'Con 5 años de residencia legal, puedes obtener un permiso permanente con plenos derechos en la UE.' },
                ],
                nacionalidad: [
                    { icon: 'ri-passport-line', title: 'Nacionalidad por Residencia', desc: 'Tras 10 años (o menos según tu caso), puedes solicitar la nacionalidad española. Analizamos tu antigüedad.' },
                    { icon: 'ri-heart-2-line', title: 'Nacionalidad por Matrimonio', desc: 'Casado/a con un/a español/a? El plazo se reduce a 1 año de residencia legal.' },
                    { icon: 'ri-file-history-line', title: 'Ley de Memoria Democrática', desc: 'Si tienes ascendientes españoles exiliados, podrías tener derecho a la nacionalidad sin residencia.' },
                ],
                familiar_reagrup: [
                    { icon: 'ri-team-line', title: 'Reagrupación Familiar', desc: 'Trae a tu cónyuge, hijos o padres a España. Los requisitos dependen de tu tipo de permiso actual.' },
                ],
                default: [
                    { icon: 'ri-compass-line', title: 'Evaluación de Opciones como Residente', desc: 'Analizamos tu situación actual para ofrecerte las mejores vías de mejora o consolidación de tu estatus.' },
                ]
            }
        };

        const situResult = results[sit] || {};
        let cards = situResult[sub] || situResult['default'] || [
            { icon: 'ri-compass-line', title: 'Consulta Personalizada', desc: 'Basándonos en tu situación específica, un abogado colegiado analizará las opciones disponibles para tu caso.' }
        ];

        const container = document.getElementById('result-cards');
        if (container) {
            container.innerHTML = cards.map((c, i) => `
                <div class="result-card" style="animation-delay: ${i * 0.1}s">
                    <i class="${c.icon} result-card-icon"></i>
                    <div class="result-card-body">
                        <strong>${c.title}</strong>
                        <p>${c.desc}</p>
                    </div>
                </div>
            `).join('');
        }
    }

    // Handle contact form submission → go to success step
    const appForm = document.getElementById('applet-form');
    if (appForm) {
        appForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = appForm.querySelector('button[type="submit"]');
            btn.innerHTML = '<i class="ri-loader-4-line ri-spin"></i> Enviando solicitud...';
            btn.disabled = true;

            setTimeout(() => {
                showStep('6');
                // Reset for next time
                btn.innerHTML = 'Enviar y contactar <i class="ri-whatsapp-line"></i>';
                btn.disabled = false;
            }, 1200);
        });
    }

    // Restart funnel logic
    function restartFunnel() {
        Object.keys(funnelAnswers).forEach(k => delete funnelAnswers[k]);
        if (appForm) appForm.reset();
        showStep('1');
    }

    // Attach to all restart buttons
    document.querySelectorAll('#restart-funnel, #restart-funnel-btn, #restart-funnel-success, #restart-funnel-final').forEach(btn => {
        btn.addEventListener('click', restartFunnel);
    });




    /* --- Exit Intent Modal --- */
    const exitModal = document.getElementById('exit-modal');
    const exitClose = document.querySelector('.exit-close');
    let modalTriggered = false;

    function showModal() {
        if (!modalTriggered) {
            exitModal.classList.add('show');
            modalTriggered = true;
        }
    }

    document.addEventListener('mouseleave', (e) => {
        if (e.clientY <= 0) showModal();
    });

    // Mobile fallback trigger (scroll past half page) — throttled to max 1 eval per 200ms
    let scrollThrottleTimer = null;
    window.addEventListener('scroll', () => {
        if (scrollThrottleTimer) return;
        scrollThrottleTimer = setTimeout(() => {
            scrollThrottleTimer = null;
            const scPct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
            if (scPct > 50 && window.innerWidth <= 768) showModal();
        }, 200);
    }, { passive: true });

    if (exitClose) {
        exitClose.addEventListener('click', () => exitModal.classList.remove('show'));
    }

    if (exitModal) {
        exitModal.addEventListener('click', (e) => {
            if (e.target === exitModal) exitModal.classList.remove('show');
        });
    }




    /* --- TextType Impl (Vanillajs port with robust init) --- */
    (function initTypingTitle() {
        const textElement = document.getElementById('presencia-text');
        const cursorRef = document.getElementById('presencia-cursor');
        const containerRef = document.getElementById('presencia-title');

        if (!textElement || !cursorRef || !containerRef) return;

        // Configuration
        const textArray = ["Presencia Internacional.", "Alcance Global.", "Asesoramiento Íntegro."];
        const typingSpeed = 75;
        const deletingSpeed = 50;
        const pauseDuration = 1500;
        const cursorBlinkDuration = 0.5;
        const loop = true;

        // Internal State
        let displayedText = "";
        let currentCharIndex = 0;
        let isDeleting = false;
        let currentTextIndex = 0;
        let timeout;

        // Limpiar el texto inicial del HTML para empezar a escribir de cero
        textElement.textContent = "";

        // 1. Cursor Animation using GSAP (may load async via defer)
        function initCursorBlink() {
            if (typeof gsap !== 'undefined') {
                gsap.set(cursorRef, { opacity: 1 });
                gsap.to(cursorRef, {
                    opacity: 0,
                    duration: cursorBlinkDuration,
                    repeat: -1,
                    yoyo: true,
                    ease: 'power2.inOut'
                });
            } else {
                cursorRef.style.animation = "cursor-blink 0.5s ease-in-out infinite alternate";
            }
        }
        // GSAP puede cargar después con defer, reintentamos brevemente
        if (typeof gsap !== 'undefined') {
            initCursorBlink();
        } else {
            const gsapCheck = setInterval(() => {
                if (typeof gsap !== 'undefined') {
                    clearInterval(gsapCheck);
                    initCursorBlink();
                }
            }, 50);
            setTimeout(() => { clearInterval(gsapCheck); initCursorBlink(); }, 2000);
        }

        // 2. Animation Logic
        function executeTypingAnimation() {
            const currentText = textArray[currentTextIndex];

            if (isDeleting) {
                if (displayedText === '') {
                    isDeleting = false;
                    currentTextIndex = (currentTextIndex + 1) % textArray.length;
                    currentCharIndex = 0;
                    timeout = setTimeout(executeTypingAnimation, 500);
                } else {
                    timeout = setTimeout(() => {
                        displayedText = displayedText.slice(0, -1);
                        textElement.textContent = displayedText;
                        executeTypingAnimation();
                    }, deletingSpeed);
                }
            } else {
                if (currentCharIndex < currentText.length) {
                    timeout = setTimeout(() => {
                        displayedText = displayedText + currentText[currentCharIndex];
                        textElement.textContent = displayedText;
                        currentCharIndex++;
                        executeTypingAnimation();
                    }, typingSpeed);
                } else {
                    if (!loop && currentTextIndex === textArray.length - 1) return;
                    timeout = setTimeout(() => {
                        isDeleting = true;
                        executeTypingAnimation();
                    }, pauseDuration);
                }
            }
        }

        // Start! (Start immediately on DOM ready instead of observer for debugging)
        setTimeout(executeTypingAnimation, 500);
    })();

    // =============================================
    // ANIMATED LIST — Especialidades
    // =============================================
    function initEspAnimatedLists() {
        document.querySelectorAll('[data-esp-list]').forEach(list => {
            const cardBody = list.closest('.esp-card-body');
            const topGrad = cardBody ? cardBody.querySelector('.esp-top-gradient') : null;
            const botGrad = cardBody ? cardBody.querySelector('.esp-bottom-gradient') : null;
            const items = Array.from(list.querySelectorAll('.esp-item'));
            const setCount = items.length;

            let selectedIndex = -1;
            let keyboardNav = false;

            // Gradientes iniciales
            if (topGrad) topGrad.style.opacity = 0;
            if (botGrad) botGrad.style.opacity = 1;

            // IntersectionObserver — anima items al entrar/salir del viewport del scroll
            const observer = new IntersectionObserver(entries => {
                entries.forEach(e => e.target.classList.toggle('in-view', e.isIntersecting));
            }, { root: list, threshold: 0.5 });
            items.forEach(item => observer.observe(item));

            // handleItemMouseEnter / click
            items.forEach((item, i) => {
                item.addEventListener('mouseenter', () => {
                    selectedIndex = i;
                    updateSelected();
                });
                item.addEventListener('click', () => {
                    selectedIndex = i;
                    updateSelected();
                });
            });

            function updateSelected() {
                items.forEach((item, i) => item.classList.toggle('selected', i === selectedIndex));
            }

            // handleScroll — gradientes
            list.addEventListener('scroll', function () {
                const { scrollTop, scrollHeight, clientHeight } = list;

                // Gradientes
                const st = list.scrollTop;
                if (topGrad) topGrad.style.opacity = Math.min(st / 50, 1);
                const bottomDist = list.scrollHeight - (st + clientHeight);
                if (botGrad) botGrad.style.opacity = Math.min(bottomDist / 50, 1);
            });

            // enableArrowNavigation — teclado
            window.addEventListener('keydown', e => {
                if (!list.matches(':hover') && !cardBody.matches(':hover')) return;

                if (e.key === 'ArrowDown' || (e.key === 'Tab' && !e.shiftKey)) {
                    e.preventDefault();
                    keyboardNav = true;
                    selectedIndex = Math.min(selectedIndex + 1, setCount - 1);
                } else if (e.key === 'ArrowUp' || (e.key === 'Tab' && e.shiftKey)) {
                    e.preventDefault();
                    keyboardNav = true;
                    selectedIndex = Math.max(selectedIndex - 1, 0);
                } else if (e.key === 'Enter' && selectedIndex >= 0) {
                    e.preventDefault();
                    console.log(items[selectedIndex].querySelector('p').textContent, selectedIndex);
                } else {
                    return;
                }
                updateSelected();

                // Scroll al item seleccionado (smooth)
                if (keyboardNav && selectedIndex >= 0) {
                    const activeItem = items[selectedIndex];
                    if (activeItem) {
                        const extraMargin = 50;
                        const itemTop = activeItem.offsetTop;
                        const itemBottom = itemTop + activeItem.offsetHeight;
                        if (itemTop < list.scrollTop + extraMargin) {
                            list.scrollTo({ top: itemTop - extraMargin, behavior: 'smooth' });
                        } else if (itemBottom > list.scrollTop + list.clientHeight - extraMargin) {
                            list.scrollTo({ top: itemBottom - list.clientHeight + extraMargin, behavior: 'smooth' });
                        }
                    }
                    keyboardNav = false;
                }
            });
        });
    }

    initEspAnimatedLists();

    // =============================================
    // CURVED LOOP MARQUEE
    // =============================================
    function initCurvedLoop() {
        const textElement = document.getElementById('text-path');
        const measureElement = document.getElementById('measure-text');
        const jacket = document.querySelector('.globe-curved-wrapper');

        if (!textElement || !measureElement || !jacket) return;

        const rawText = "🇲🇦 🇷🇴 🇨🇴 🇪🇨 🇻🇪 🇦🇷 🇵🇪 🇨🇳 🇬🇧 🇮🇹 🇵🇰 🇭🇳 🇩🇴 🇧🇴 🇧🇷 🇸🇳 ";
        const hasTrailing = /\s|\u00A0$/.test(rawText);
        const text = (hasTrailing ? rawText.replace(/\s+$/, '') : rawText) + '\u00A0';

        measureElement.textContent = text;

        // Let the font paint accurately before measuring
        setTimeout(() => {
            const spacing = measureElement.getComputedTextLength() || 400; // fallback

            const totalText = spacing ? Array(Math.ceil(1800 / spacing) + 2).fill(text).join('') : text;
            textElement.textContent = totalText;

            const speed = 0.8; // slow interaction initially
            let offset = -spacing;
            let direction = 'left';
            textElement.setAttribute('startOffset', offset + 'px');

            let drag = false;
            let lastX = 0;
            let vel = 0;
            let frame = null;

            const step = () => {
                if (!drag) {
                    const delta = direction === 'right' ? speed : -speed;
                    offset += delta;

                    const wrapPoint = spacing;
                    if (offset <= -wrapPoint) offset += wrapPoint;
                    if (offset > 0) offset -= wrapPoint;

                    textElement.setAttribute('startOffset', offset + 'px');
                }
                frame = requestAnimationFrame(step);
            };
            frame = requestAnimationFrame(step);

            jacket.style.visibility = 'visible';
        }, 100);
    }

    if (document.fonts) {
        document.fonts.ready.then(initCurvedLoop);
    } else {
        setTimeout(initCurvedLoop, 600);
    }

    // =============================================
    // ROTATING TEXT - Ciudades de España
    // =============================================
    function initRotatingText() {
        const texts = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Málaga', 'Zaragoza', 'Murcia', 'Bilbao', 'Alicante'];
        const container = document.getElementById('rotating-text');
        if (!container) return;
        
        let currentIndex = 0;
        let isAnimating = false;

        function renderText(index) {
            isAnimating = true;
            const text = texts[index];
            container.innerHTML = '';

            // Create spans for each character
            text.split('').forEach((char) => {
                const span = document.createElement('span');
                span.textContent = char;
                span.style.display = 'inline-block';
                if (char === ' ') {
                    span.style.whiteSpace = 'pre';
                }
                container.appendChild(span);
            });

            const chars = container.querySelectorAll('span');
            if (typeof gsap !== 'undefined') {
                gsap.fromTo(chars, 
                    { y: "150%", opacity: 0 },
                    { 
                        y: "0%", 
                        opacity: 1, 
                        duration: 0.35, 
                        stagger: {
                            amount: 0.1, 
                            from: "end" 
                        },
                        ease: "back.out(1.5)",
                        onComplete: () => { isAnimating = false; }
                    }
                );
            }
        }

        function rotate() {
            if (isAnimating) return;
            const chars = container.querySelectorAll('span');
            if (typeof gsap !== 'undefined') {
                isAnimating = true;
                gsap.to(chars, {
                    y: "-120%", 
                    opacity: 0, 
                    duration: 0.3, 
                    stagger: {
                        amount: 0.1,
                        from: "end"
                    },
                    ease: "power2.in",
                    onComplete: () => {
                        currentIndex = (currentIndex + 1) % texts.length;
                        renderText(currentIndex);
                    }
                });
            }
        }

        // Initial render
        renderText(currentIndex);

        // Interval rotatorio
        setInterval(rotate, 1800);
    }
    initRotatingText();

});

// Mobile Menu Functions
window.toggleMobileMenu = function() {
    const nav = document.getElementById('mobile-nav');
    if (nav) {
        nav.classList.toggle('active');
        document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
    }
};

window.toggleMobileDropdown = function(e) {
    const btn = e.currentTarget;
    const wrapper = btn.closest('.mobile-nav-dropdown-wrapper');
    if (wrapper) {
        wrapper.classList.toggle('open');
    }
};
