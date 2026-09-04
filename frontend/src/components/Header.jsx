import { useState } from 'react'
import logo from '../assets/logo2.png'
import Button from './Button'


function Header() {
    const [isOpen, setIsOpen] = useState(false);

    const scrollToSection = (id) => {
        document.getElementById(id)?.scrollIntoView({
            behavior: "smooth",
        });

        setIsOpen(false);
    };

    return (
        <header className="sticky top-0 z-50 border-b border-slate-700  bg-slate-900 backdrop-blur">
            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">

                {/* Logo */}
                <div className="flex items-center">
                    <a href="#" className="flex items-center">
                        <img src={logo} alt="Logo" className="h-8 w-auto" />
                    </a>
                </div>

                {/* Desktop Navigation */}
                <nav className="hidden items-center gap-8 md:flex">
                    <Button
                        onClick={() => scrollToSection("how-it-works")}
                        variant="nav"
                    >
                        How It Works
                    </Button>

                    <Button
                        onClick={() => scrollToSection("features")}
                        variant="nav">
                        Features
                    </Button>

                    <Button
                        onClick={() => scrollToSection("about")}
                        variant="nav"
                    >
                        About
                    </Button>
                </nav>

                {/* Desktop Auth */}
                <div className="hidden items-center gap-3 md:flex">
                    <Button variant="login">
                        Login
                    </Button>

                    <Button variant="signup">
                        Sign Up
                    </Button>
                </div>

                {/* Mobile Hamburger */}
                <Button
                    onClick={() => setIsOpen(!isOpen)}
                    variant="icon"
                    aria-label="Toggle navigation"
                >
                    {isOpen ? (
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            strokeWidth="2"
                            stroke="currentColor"
                            className="h-5 w-5"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M6 18L18 6M6 6l12 12"
                            />
                        </svg>
                    ) : (
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            strokeWidth="2"
                            stroke="currentColor"
                            className="h-5 w-5"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M4 6h16M4 12h16M4 18h16"
                            />
                        </svg>
                    )}
                </Button>
            </div>

            {/* Mobile Menu */}
            {isOpen && (
                <div className="border-t border-slate-800 bg-slate-900 md:hidden">
                    <div className="mx-auto max-w-7xl px-4 py-5 sm:px-6">

                        <div className="flex flex-col gap-1">

                            <Button
                                onClick={() => scrollToSection("how-it-works")}
                                variant="tertiary"
                            >
                                How It Works
                            </Button>

                            <Button
                                onClick={() => scrollToSection("features")}
                                variant="tertiary"
                            >
                                Features
                            </Button>

                            <Button
                                onClick={() => scrollToSection("about")}
                                variant="tertiary"
                            >
                                About
                            </Button>

                            <div className="my-3 border-t border-gray-200" />

                            <Button variant="tertiary">
                                Login
                            </Button>

                            <Button variant="mobileSignup">
                                Sign Up
                            </Button>

                        </div>
                    </div>
                </div>
            )}
        </header>
    );
}

export default Header;





