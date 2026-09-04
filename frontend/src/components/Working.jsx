function HowItWorks() {
  const steps = [
    {
      step: "01",
      title: "Create an account",
      text: "Sign up and access your personalized stock analysis dashboard.",
    },
    {
      step: "02",
      title: "Choose a stock",
      text: "Search for the stock you want to analyze using the platform.",
    },
    {
      step: "03",
      title: "Analyze the market",
      text: "Explore historical data, trends, charts, and other useful indicators.",
    },
    {
      step: "04",
      title: "Get AI insights",
      text: "Our prediction model processes the available data and provides an AI-assisted prediction.",
    },
  ];

  return (
    <section id="how-it-works" className="bg-white py-20 md:py-24">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

        <div className="mx-auto max-w-2xl text-center">
          <p className="text-sm font-semibold uppercase tracking-wider text-gray-500">
            How It Works
          </p>

          <h2 className="mt-3 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            From stock selection to AI insight.
          </h2>

          <p className="mt-4 text-gray-600">
            The process is designed to keep stock analysis simple and
            understandable.
          </p>
        </div>

        <div className="mt-14 grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          {steps.map((step) => (
            <div key={step.step} className="relative">

              <div className="text-5xl font-bold text-gray-100">
                {step.step}
              </div>

              <h3 className="relative -mt-5 text-lg font-semibold text-gray-900">
                {step.title}
              </h3>

              <p className="mt-3 text-sm leading-6 text-gray-600">
                {step.text}
              </p>

            </div>
          ))}
        </div>

      </div>
    </section>
  );
}

export default HowItWorks;