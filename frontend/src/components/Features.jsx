function Features() {
    const features = [
        {
            number: "01",
            title: "AI-Powered Analysis",
            description:
                "Use machine learning models to analyze historical market data and identify potential patterns.",
        },
        {
            number: "02",
            title: "Market Insights",
            description:
                "Understand market movements through simple and meaningful data-driven insights.",
        },
        {
            number: "03",
            title: "Interactive Charts",
            description:
                "Visualize stock performance and trends through clean and easy-to-understand charts.",
        },
        {
            number: "04",
            title: "Smart Predictions",
            description:
                "Get AI-generated predictions based on historical data and selected stocks.",
        },
    ];

    return (
        <section id="features" className="bg-gray-50 py-20 md:py-24">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

                <div className="max-w-2xl">
                    <p className="text-sm font-semibold uppercase tracking-wider text-gray-500">
                        Features
                    </p>

                    <h2 className="mt-3 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
                        Everything you need to understand the market.
                    </h2>

                    <p className="mt-4 text-gray-600">
                        A simple interface combined with powerful data analysis and
                        machine learning.
                    </p>
                </div>

                <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
                    {features.map((feature) => (
                        <div
                            key={feature.number}
                            className="rounded-xl border border-gray-200 bg-white p-6 transition hover:-translate-y-1 hover:shadow-md"
                        >
                            <span className="text-sm font-semibold text-gray-400">
                                {feature.number}
                            </span>

                            <h3 className="mt-8 text-lg font-semibold text-gray-900">
                                {feature.title}
                            </h3>

                            <p className="mt-3 text-sm leading-6 text-gray-600">
                                {feature.description}
                            </p>
                        </div>
                    ))}
                </div>

            </div>
        </section>
    );
}

export default Features;