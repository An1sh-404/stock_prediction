import Button from './Button'


function CTA() {
    return (
        <section id="about" className="bg-black py-20 text-white md:py-24">
            <div className="mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">

                <p className="text-sm font-semibold uppercase tracking-wider text-gray-400">
                    Start Exploring
                </p>

                <h2 className="mt-4 text-3xl font-bold tracking-tight sm:text-4xl lg:text-5xl">
                    Turn market data into meaningful insights.
                </h2>

                <p className="mx-auto mt-5 max-w-2xl text-gray-400">
                    Create your account and explore AI-assisted stock analysis,
                    charts, trends, and predictions.
                </p>
                <Button variant="secondary" className="mt-8 bg-white px-7 py-3">
                    Create Your Account
                </Button>

            </div>
        </section>
    );
}

export default CTA;