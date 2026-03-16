"use client";

import { useState } from "react";
import { ShineBorder } from "@/registry/magicui/shine-border";
import GlobeWithFlags from "@/components/GlobeWithFlags";
import CurvedLoop from "@/components/CurvedLoop";

const GOLD = "#C9A84C";

type Step = {
  question: string;
  prefix: string;
  options: { icon: React.ReactNode; label: string; sublabel: string }[];
};

const steps: Step[] = [
  {
    prefix: "Antes de empezar,",
    question: "¿para quién es el análisis?",
    options: [
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <circle cx="12" cy="8" r="4" /><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7" />
          </svg>
        ),
        label: "Es para mí",
        sublabel: "Quiero conocer mis opciones legales",
      },
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <circle cx="9" cy="7" r="3.5" /><path d="M2 20c0-3.5 3-6 7-6s7 2.5 7 6" />
            <circle cx="17" cy="8" r="2.5" /><path d="M17.5 14c1.7.3 4 1.5 4 4" />
          </svg>
        ),
        label: "Es para un familiar",
        sublabel: "Quiero ayudar a un familiar",
      },
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
          </svg>
        ),
        label: "Es para un amigo/a",
        sublabel: "Quiero ayudar a alguien cercano",
      },
    ],
  },
  {
    prefix: "Cuéntanos,",
    question: "¿cuál es tu situación principal?",
    options: [
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <rect x="3" y="3" width="18" height="18" rx="2" /><path d="M3 9h18M9 21V9" />
          </svg>
        ),
        label: "Problema laboral",
        sublabel: "Despido, reclamación o conflicto con empresa",
      },
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /><polyline points="9 22 9 12 15 12 15 22" />
          </svg>
        ),
        label: "Asunto familiar / herencia",
        sublabel: "Divorcio, custodia o sucesión",
      },
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" />
          </svg>
        ),
        label: "Otro tipo de conflicto",
        sublabel: "Penal, civil, administrativo u otro",
      },
    ],
  },
  {
    prefix: "Por último,",
    question: "¿con qué urgencia necesitas ayuda?",
    options: [
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" /><polyline points="12 6 12 12 16 14" />
          </svg>
        ),
        label: "Es urgente",
        sublabel: "Necesito ayuda lo antes posible",
      },
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <rect x="3" y="4" width="18" height="18" rx="2" /><line x1="16" y1="2" x2="16" y2="6" /><line x1="8" y1="2" x2="8" y2="6" /><line x1="3" y1="10" x2="21" y2="10" />
          </svg>
        ),
        label: "En las próximas semanas",
        sublabel: "Tengo algo de tiempo para valorar opciones",
      },
      {
        icon: (
          <svg width="22" height="22" fill="none" stroke={GOLD} strokeWidth="1.5" viewBox="0 0 24 24">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
          </svg>
        ),
        label: "Solo quiero informarme",
        sublabel: "Estoy explorando mis opciones legales",
      },
    ],
  },
];

export default function Home() {
  const [currentStep, setCurrentStep] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [done, setDone] = useState(false);

  const step = steps[currentStep];
  const totalSteps = steps.length;

  function handleSelect(idx: number) {
    setSelected(idx);
    setTimeout(() => {
      if (currentStep < totalSteps - 1) {
        setCurrentStep((s) => s + 1);
        setSelected(null);
      } else {
        setDone(true);
      }
    }, 350);
  }

  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center px-4 py-12 gap-0"
      style={{ background: "#0a0a0a" }}
    >
      {/* Globe with curved flag text behind it */}
      <GlobeWithFlags />
      {/* CurvedLoop + Card wrapper */}
      <div className="relative w-full max-w-2xl">
        {/* Curved text behind card */}
        <div
          className="absolute left-1/2 -translate-x-1/2 w-[140%] pointer-events-none"
          style={{ top: "40%", zIndex: 0 }}
        >
          <CurvedLoop
            marqueeText="ÉXITO ✦ 100% ✦ GARANTIZADO ✦ "
            speed={2}
            curveAmount={200}
            direction="right"
            interactive={false}
          />
        </div>

      {/* Card box */}
      <div
        className="relative w-full rounded-2xl p-10 flex flex-col gap-8 overflow-hidden"
        style={{ zIndex: 1 }}
        style={{
          background: "#111111",
          boxShadow: "0 8px 48px 0 rgba(0,0,0,0.6)",
        }}
      >
        <ShineBorder shineColor={["#C9A84C", "#F0D080", "#A07830"]} duration={10} borderWidth={1.5} />
        {/* Title */}
        <h1
          className="text-3xl sm:text-4xl font-semibold leading-tight"
          style={{ color: "#fff", fontFamily: "sans-serif" }}
        >
          Realiza este diagnóstico gratuito{" "}
          <span style={{ color: GOLD }}>en menos de 1 minuto</span>
        </h1>

        {/* Progress bar */}
        <div className="flex items-center gap-3">
          <div
            className="h-[2px] flex-1 rounded-full overflow-hidden"
            style={{ background: "#2a2a2a" }}
          >
            <div
              className="h-full rounded-full transition-all duration-500"
              style={{
                background: GOLD,
                width: `${((currentStep + (done ? 1 : 0)) / totalSteps) * 100}%`,
              }}
            />
          </div>
          <span className="text-xs font-medium" style={{ color: "#888" }}>
            Paso {done ? totalSteps : currentStep + 1} de {totalSteps}
          </span>
        </div>

        {done ? (
          /* Final screen */
          <div className="flex flex-col items-center gap-6 py-8 text-center">
            <div
              className="w-16 h-16 rounded-full flex items-center justify-center"
              style={{ background: "#1a1a1a", border: `1px solid ${GOLD}` }}
            >
              <svg width="28" height="28" fill="none" stroke={GOLD} strokeWidth="2" viewBox="0 0 24 24">
                <polyline points="20 6 9 17 4 12" />
              </svg>
            </div>
            <h2
              className="text-2xl font-semibold"
              style={{ fontFamily: "var(--font-playfair)", color: "#fff" }}
            >
              ¡Gracias por completar el diagnóstico!
            </h2>
            <p className="text-sm leading-6" style={{ color: "#888" }}>
              Uno de nuestros abogados se pondrá en contacto contigo en menos de 24 horas para presentarte tus opciones legales.
            </p>
            <a
              href="https://wa.me/34600000000"
              className="mt-2 px-8 py-3 rounded-full text-sm font-semibold transition-opacity hover:opacity-80"
              style={{ background: GOLD, color: "#000" }}
            >
              Hablar con un abogado ahora
            </a>
          </div>
        ) : (
          <>
            {/* Question title */}
            <h2
              className="text-xl sm:text-2xl font-medium leading-snug"
              style={{ color: "#fff", fontFamily: "sans-serif" }}
            >
              {step.prefix}{" "}
              <span style={{ color: "#ccc" }}>
                {step.question}
              </span>
            </h2>

            {/* Options */}
            <div className="flex flex-col gap-3">
              {step.options.map((opt, idx) => (
                <button
                  key={idx}
                  onClick={() => handleSelect(idx)}
                  className="flex items-center gap-4 rounded-xl px-5 py-4 text-left transition-all duration-200 cursor-pointer"
                  style={{
                    background: selected === idx ? "#1c1a12" : "#181818",
                    border: `1px solid ${selected === idx ? GOLD : "#2a2a2a"}`,
                    outline: "none",
                  }}
                  onMouseEnter={(e) => {
                    if (selected !== idx)
                      (e.currentTarget as HTMLButtonElement).style.border = `1px solid #444`;
                  }}
                  onMouseLeave={(e) => {
                    if (selected !== idx)
                      (e.currentTarget as HTMLButtonElement).style.border = `1px solid #2a2a2a`;
                  }}
                >
                  <span className="shrink-0">{opt.icon}</span>
                  <span className="flex flex-col gap-0.5">
                    <span className="text-xs font-medium" style={{ color: "#fff", fontFamily: "sans-serif" }}>
                      {opt.label}
                    </span>
                    <span className="text-[11px]" style={{ color: "#888", fontFamily: "sans-serif" }}>
                      {opt.sublabel}
                    </span>
                  </span>
                </button>
              ))}
            </div>

            {/* Bottom badges */}
            <div className="flex flex-wrap gap-2 pt-1">
              {[
                { icon: "🛡", label: "100% Confidencial" },
                { icon: "⏱", label: "Solo 1 minuto" },
                { icon: "$", label: "Sin compromiso" },
              ].map((badge) => (
                <span
                  key={badge.label}
                  className="flex items-center gap-1.5 rounded-full px-3 py-1.5 text-xs font-medium"
                  style={{
                    background: "#181818",
                    border: "1px solid #2a2a2a",
                    color: "#888",
                  }}
                >
                  <span style={{ color: GOLD }}>{badge.icon}</span>
                  {badge.label}
                </span>
              ))}
            </div>
          </>
        )}
      </div>
      </div>
    </div>
  );
}
