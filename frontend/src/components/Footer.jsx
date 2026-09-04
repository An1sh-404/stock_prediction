


function Footer() {
    return (
        <footer className="bg-white">
            <div className="mx-auto max-w-7xl flex align-center justify-center gap-6 px-4 py-8 sm:px-6 lg:px-8">

                {/* Logo */}
                {/* <div className="flex justify-center bg-slate-900 h-8 w-28 items-center rounded-md border-1 border-b border-gray-300 text-xs text-gray-400">

                    <img src={logo} alt="Logo" className="h-6 w-auto fill-current" />
                </div> */}

                <p className=" text-sm text-gray-500">
                    © Made with ❤️ by <a href="https://github.com/An1sh-404" target="_blank" rel="noopener noreferrer" className="text-s  text-blue-400 hover:text-blue-600">An1sh-404</a>.
                </p>

                {/* <div className="flex gap-5 text-sm text-gray-500">
                    <a href="#" className="hover:text-black">
                        Privacy
                    </a>

                    <a href="#" className="hover:text-black">
                        Terms
                    </a>

                    <a href="#" className="hover:text-black">
                        Contact
                    </a>
                </div> */}

            </div>
        </footer>
    );
}

export default Footer;