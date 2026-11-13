
import './App.css'

import Header from './components/Header'
import Main from './components/Main'
import Features from './components/Features'
import HowItWorks from './components/Working'
import Stats from './components/Stats'
import CTA from './components/CreateAccount'
import Footer from './components/Footer'
import Register from './components/Register'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {


  return (
    <>

        <>

      <div className="min-h-screen bg-slate-950 text-white">
        <Header />
        <main>
          <Main />
          <Features />
          <HowItWorks />
          <Stats />
          <CTA />




        </main>
        <Footer />

      </div>


    </>
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
        </Routes>
      </Router>


    </>

  )
}

export default App
