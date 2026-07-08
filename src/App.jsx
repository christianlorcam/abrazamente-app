import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Heart, Activity, BookOpen, Calendar, Shield, Sparkles, X, ChevronRight } from 'lucide-react';
import BreathingTimer from './features/breathing/BreathingTimer';
import GroundingWizard from './features/grounding/GroundingWizard';
import MoodTracker from './features/journal/MoodTracker';
// import ProfessionalDirectory from './features/professionals/ProfessionalDirectory';

export default function App() {
  const [activeModal, setActiveModal] = useState(null); // 'botiquin', 'journal', 'professionals'
  const [botiquinTab, setBotiquinTab] = useState('breathing'); // 'breathing', 'grounding'

  // Scroll handler for landing sections
  const scrollToId = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="relative min-h-screen text-gray-100 selection:bg-indigo-500/30 selection:text-indigo-200">
      
      {/* Background Decorative Gradients */}
      <div className="absolute top-0 left-0 w-full h-[600px] overflow-hidden pointer-events-none z-0">
        <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] rounded-full bg-blue-500/10 blur-[120px]" />
        <div className="absolute top-[20%] right-[-10%] w-[45%] h-[45%] rounded-full bg-pink-500/10 blur-[120px]" />
      </div>

      {/* Header / Navbar */}
      <header className="sticky top-0 z-40 bg-gray-950/40 backdrop-blur-md border-b border-white/5">
        <div className="max-w-6xl mx-auto px-6 h-20 flex justify-between items-center">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => scrollToId('hero')}>
            <div className="w-10 h-10 rounded-xl bg-blue-600/25 border border-blue-500/35 flex items-center justify-center text-blue-400">
              <Heart className="w-5 h-5 fill-current" />
            </div>
            <span className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-blue-400 to-indigo-300 bg-clip-text text-transparent">
              AbrazaMente
            </span>
          </div>

          <nav className="hidden md:flex items-center gap-8 text-sm font-semibold text-gray-400">
            <button onClick={() => scrollToId('features')} className="hover:text-white transition-colors cursor-pointer">Ecosistema</button>
            <button onClick={() => { setActiveModal('professionals') }} className="hover:text-white transition-colors cursor-pointer">Especialistas</button>
            <button onClick={() => { setActiveModal('journal') }} className="hover:text-white transition-colors cursor-pointer">Diario</button>
            <button onClick={() => { setActiveModal('botiquin') }} className="hover:text-white transition-colors cursor-pointer">Botiquín</button>
          </nav>

          <button
            onClick={() => setActiveModal('professionals')}
            className="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-sm shadow-lg shadow-blue-600/20 transition-all active:scale-95 cursor-pointer"
          >
            Comenzar Proceso
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <section id="hero" className="max-w-6xl mx-auto px-6 pt-16 pb-12 z-10 relative flex flex-col md:flex-row items-center gap-12">
        <div className="flex-1 flex flex-col items-start gap-6 text-left">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/20 text-xs font-bold text-blue-400 shadow-md">
            <Sparkles className="w-3.5 h-3.5 fill-current" />
            Tu espacio seguro de salud mental
          </div>
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-black text-white leading-tight tracking-tight">
            Encuentra la paz <br />
            <span className="bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
              que mereces hoy.
            </span>
          </h1>
          <p className="text-gray-400 text-base md:text-lg leading-relaxed max-w-lg">
            AbrazaMente te conecta con especialistas validados clínicamente y te brinda herramientas inmediatas de respiración y grounding para gestionar la ansiedad en segundos.
          </p>
          <div className="flex flex-wrap gap-4 mt-2">
            <button
              onClick={() => setActiveModal('botiquin')}
              className="flex items-center gap-2 px-6 py-3.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold shadow-lg shadow-blue-600/30 transition-all active:scale-95 cursor-pointer"
            >
              Probar Botiquín de Emergencia <ChevronRight className="w-4 h-4" />
            </button>
            <button
              onClick={() => scrollToId('features')}
              className="px-6 py-3.5 rounded-xl bg-white/5 hover:bg-white/10 text-gray-300 font-bold border border-white/10 transition-all active:scale-95 cursor-pointer"
            >
              Explorar Ecosistema
            </button>
          </div>
        </div>

        <div className="flex-1 w-full flex justify-center relative">
          <div className="w-72 h-72 md:w-80 md:h-80 rounded-[40px] bg-gradient-to-tr from-blue-600 to-indigo-700 p-8 flex flex-col justify-between text-white relative shadow-2xl overflow-hidden group">
            <div className="absolute inset-0 bg-radial from-white/10 to-transparent pointer-events-none" />
            <div className="flex justify-between items-start">
              <div className="w-12 h-12 rounded-2xl bg-white/15 border border-white/25 flex items-center justify-center">
                <Heart className="w-6 h-6 fill-white" />
              </div>
              <span className="text-xs font-bold bg-white/20 px-3 py-1 rounded-full uppercase tracking-wider">
                MVP v1.0
              </span>
            </div>
            <div>
              <h3 className="text-2xl font-black mb-2 leading-snug">Salud Mental de Calidad</h3>
              <p className="text-xs text-white/70 leading-relaxed">
                Herramientas clínicas diseñadas para brindarte alivio inmediato y continuo.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Trust wrapper bar */}
      <section className="max-w-6xl mx-auto px-6 py-6 z-10 relative">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 bg-white/2 border border-white/5 rounded-3xl p-6 backdrop-blur-xl">
          <div className="flex items-center gap-4">
            <div className="w-11 h-11 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
              <Shield className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white">Privacidad Asegurada</h4>
              <p className="text-xs text-gray-400 mt-0.5">Datos encriptados de extremo a extremo.</p>
            </div>
          </div>
          <div className="flex items-center gap-4 border-t md:border-t-0 md:border-x border-white/5 pt-4 md:pt-0 md:px-6">
            <div className="w-11 h-11 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
              <Activity className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white">Especialistas Verificados</h4>
              <p className="text-xs text-gray-400 mt-0.5">Profesionales certificados con licencia activa.</p>
            </div>
          </div>
          <div className="flex items-center gap-4 border-t md:border-t-0 border-white/5 pt-4 md:pt-0 md:pl-6">
            <div className="w-11 h-11 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
              <Heart className="w-5 h-5" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-white">Espacio de Alivio</h4>
              <p className="text-xs text-gray-400 mt-0.5">Ejercicios validados y asistencia sin juicios.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Ecosistema (Bento grid) */}
      <section id="features" className="max-w-6xl mx-auto px-6 py-16 z-10 relative">
        <div className="text-center mb-12">
          <div className="text-xs font-bold text-blue-400 uppercase tracking-widest mb-2">Nuestro Ecosistema</div>
          <h2 className="text-3xl md:text-4xl font-extrabold text-white">Diseñado para tu bienestar</h2>
          <p className="text-gray-400 mt-3 text-sm md:text-base max-w-xl mx-auto leading-relaxed">
            Explora las funcionalidades principales que componen el MVP funcional de AbrazaMente.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Card 1: Professionals */}
          <div
            onClick={() => setActiveModal('professionals')}
            className="bg-white/2 border border-white/5 rounded-3xl p-6 hover:border-blue-500/30 hover:bg-white/4 transition-all duration-300 cursor-pointer flex flex-col justify-between min-h-[220px] group"
          >
            <div className="w-12 h-12 rounded-2xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400 group-hover:scale-110 transition-transform">
              <Calendar className="w-6 h-6" />
            </div>
            <div className="mt-8">
              <h3 className="text-lg font-bold text-white mb-2">Terapia Profesional</h3>
              <p className="text-xs text-gray-400 leading-relaxed">
                Encuentra psicólogos y psiquiatras según tu especialidad y agenda una cita virtual en segundos.
              </p>
            </div>
          </div>

          {/* Card 2: Emotional First-Aid Toolkit */}
          <div
            onClick={() => setActiveModal('botiquin')}
            className="bg-white/2 border border-white/5 rounded-3xl p-6 hover:border-emerald-500/30 hover:bg-white/4 transition-all duration-300 cursor-pointer flex flex-col justify-between min-h-[220px] group"
          >
            <div className="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform">
              <Activity className="w-6 h-6" />
            </div>
            <div className="mt-8">
              <h3 className="text-lg font-bold text-white mb-2">Herramientas Emocionales</h3>
              <p className="text-xs text-gray-400 leading-relaxed">
                Accede al botiquín instantáneo de respiración cuadrada y ejercicios cognitivos de grounding 5-4-3-2-1.
              </p>
            </div>
          </div>

          {/* Card 3: Journaling (Mood Tracker) */}
          <div
            onClick={() => setActiveModal('journal')}
            className="bg-white/2 border border-white/5 rounded-3xl p-6 hover:border-indigo-500/30 hover:bg-white/4 transition-all duration-300 cursor-pointer flex flex-col justify-between min-h-[220px] group"
          >
            <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 group-hover:scale-110 transition-transform">
              <BookOpen className="w-6 h-6" />
            </div>
            <div className="mt-8">
              <h3 className="text-lg font-bold text-white mb-2">Diario Emocional</h3>
              <p className="text-xs text-gray-400 leading-relaxed">
                Registra tu humor diario, escribe tus reflexiones y haz un seguimiento de tu paz mental a lo largo del tiempo.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Floating Action Button (FAB) for immediate Emotional Toolkit */}
      <button
        onClick={() => setActiveModal('botiquin')}
        className="fixed bottom-6 right-6 z-30 flex items-center gap-2.5 px-5 py-3 rounded-full bg-blue-600 hover:bg-blue-500 text-white font-bold text-sm shadow-xl shadow-blue-600/30 transition-all hover:translate-y-[-2px] active:translate-y-0 cursor-pointer border border-white/10 group"
      >
        <Heart className="w-4 h-4 fill-red-400 stroke-red-400 group-hover:scale-125 transition-transform" />
        <span>Botiquín Emocional</span>
      </button>

      {/* Modal Wrapper AnimatePresence */}
      <AnimatePresence>
        {activeModal && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            {/* Dark blur backdrop */}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setActiveModal(null)}
              className="absolute inset-0 bg-black/60 backdrop-blur-md"
            />

            {/* Modal Card content */}
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 15 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 15 }}
              transition={{ type: "spring", damping: 25, stiffness: 350 }}
              className="bg-gray-900 border border-white/10 rounded-3xl w-full max-w-3xl max-h-[90vh] overflow-y-auto z-10 flex flex-col shadow-2xl relative scrollable"
            >
              
              {/* Header */}
              <div className="p-6 border-b border-white/5 flex justify-between items-center">
                <div>
                  <h2 className="text-xl font-extrabold text-white flex items-center gap-2">
                    {activeModal === 'botiquin' && 'Botiquín de Apoyo Inmediato'}
                    {activeModal === 'journal' && 'Tu Diario Emocional Express'}
                    {activeModal === 'professionals' && 'Directorio de Terapeutas'}
                  </h2>
                  <p className="text-xs text-gray-400 mt-1">
                    {activeModal === 'botiquin' && 'Técnicas inmediatas para momentos de crisis y ansiedad.'}
                    {activeModal === 'journal' && 'Monitorea tu estado de ánimo de forma privada.'}
                    {activeModal === 'professionals' && 'Agenda atención con profesionales verificados.'}
                  </p>
                </div>
                <button
                  onClick={() => setActiveModal(null)}
                  className="w-9 h-9 rounded-full bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white flex items-center justify-center transition-all cursor-pointer"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Tabs for Botiquín */}
              {activeModal === 'botiquin' && (
                <div className="flex bg-white/2 border-b border-white/5 px-6 gap-6">
                  <button
                    onClick={() => setBotiquinTab('breathing')}
                    className={`py-3.5 text-xs font-bold border-b-2 transition-all cursor-pointer ${
                      botiquinTab === 'breathing' ? 'border-blue-500 text-blue-400' : 'border-transparent text-gray-400 hover:text-white'
                    }`}
                  >
                    Respiración Guiada (Box Breathing)
                  </button>
                  <button
                    onClick={() => setBotiquinTab('grounding')}
                    className={`py-3.5 text-xs font-bold border-b-2 transition-all cursor-pointer ${
                      botiquinTab === 'grounding' ? 'border-blue-500 text-blue-400' : 'border-transparent text-gray-400 hover:text-white'
                    }`}
                  >
                    Ejercicio de Grounding 5-4-3-2-1
                  </button>
                </div>
              )}

              <div className="p-6 overflow-y-auto">
                {activeModal === 'botiquin' && botiquinTab === 'breathing' && <BreathingTimer />}
                {activeModal === 'botiquin' && botiquinTab === 'grounding' && <GroundingWizard />}
                {activeModal === 'journal' && <MoodTracker />}
                {activeModal === 'professionals' && <div className="text-center py-12 text-gray-400 text-sm">El Directorio de Especialistas se implementará en la siguiente fase (feature/clinician-directory).</div>}
              </div>

            </motion.div>
          </div>
        )}
      </AnimatePresence>

      {/* Footer */}
      <footer className="border-t border-white/5 py-8 mt-16 bg-gray-950/20 text-center text-xs text-gray-500">
        <p>© 2026 AbrazaMente. Creado con amor para tu salud mental.</p>
      </footer>

    </div>
  );
}
