function Stats() {
  return (
    <section className="border-y border-gray-200 bg-gray-50">
      <div className="mx-auto grid max-w-7xl divide-y divide-gray-200 px-4 py-12 sm:px-6 md:grid-cols-3 md:divide-x md:divide-y-0 lg:px-8">

        <div className="px-6 py-4 text-center">
          <p className="text-3xl font-bold text-gray-900">
            50K+
          </p>
          <p className="mt-2 text-sm text-gray-500">
            Market data points
          </p>
        </div>

        <div className="px-6 py-4 text-center">
          <p className="text-3xl font-bold text-gray-900">
            AI
          </p>
          <p className="mt-2 text-sm text-gray-500">
            Machine learning insights
          </p>
        </div>

        <div className="px-6 py-4 text-center">
          <p className="text-3xl font-bold text-gray-900">
            24/7
          </p>
          <p className="mt-2 text-sm text-gray-500">
            Market analysis
          </p>
        </div>

      </div>
    </section>
  );
}

export default Stats;