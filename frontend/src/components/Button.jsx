const variantClasses = {
    primary: 'rounded-lg bg-black px-6 py-3 text-sm font-semibold text-white transition hover:bg-gray-800',
    secondary: 'rounded-lg border border-gray-300 px-6 py-3 text-sm font-semibold text-black transition hover:bg-gray-200',
    tertiary: 'rounded-lg px-3 py-3 text-left text-sm font-medium text-gray-400 transition hover:bg-slate-800 hover:text-white',
    nav: 'text-sm font-medium text-gray-400 transition hover:text-white',
    login: 'rounded-lg border border-gray-500 bg-slate-700 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-800',
    signup: 'rounded-lg border border-gray-500 bg-emerald-500 px-4 py-2 text-sm font-medium text-slate-950 transition hover:bg-emerald-700',
    mobileSignup: 'mt-1 rounded-lg bg-emerald-400 px-4 py-3 text-sm font-medium text-slate-950 transition hover:bg-emerald-500',
    icon: 'flex h-10 w-10 items-center justify-center rounded-lg border border-slate-600 text-gray-200 transition hover:bg-slate-800 md:hidden',
};
function Button({ children, variant, className = '', type = 'button', ...props }) {
    return (
        <button
            type={type}
            className={`${variantClasses[variant] ?? ''} ${className}`.trim()}
            {...props}
        >
            {children}
        </button>
    );
}

export default Button;
