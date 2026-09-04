import Button from './Button'

function Hero() {
    return (
        <section className="overflow-hidden bg-white">
            <div className="mx-auto grid max-w-7xl items-center gap-14 px-4 py-20 sm:px-6 md:py-28 lg:grid-cols-2 lg:px-8">

                
                <div>
                    <div className="mb-6 inline-flex items-center rounded-full border border-gray-200 bg-gray-50 px-4 py-2 text-sm text-gray-600">
                        AI-powered market insights
                    </div>

                    <h1 className="max-w-2xl text-4xl font-bold leading-tight tracking-tight text-gray-900 sm:text-5xl lg:text-6xl">
                        Make smarter decisions with
                        <span className="block text-gray-500">
                            AI-powered stock predictions.
                        </span>
                    </h1>

                    <p className="mt-6 max-w-xl text-base leading-7 text-gray-600 sm:text-lg">
                        Analyze market data, discover trends, and gain intelligent
                        insights to help you make more informed investment decisions.
                    </p>

                    <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                        <Button variant="primary">
                            Get Started
                        </Button>

                        <Button
                            onClick={() =>
                                document
                                    .getElementById("how-it-works")
                                    ?.scrollIntoView({ behavior: "smooth" })
                            }
                            variant="secondary"
                        >
                            See How It Works
                        </Button>
                    </div>

                    <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3 text-sm text-gray-500">
                        <span>✓ Data-driven analysis</span>
                        <span>✓ AI-assisted insights</span>
                        <span>✓ Easy to use</span>
                    </div>
                </div>

               
                <div className="relative">
                    <div className="rounded-2xl border border-gray-200 bg-gray-50 p-4 shadow-sm sm:p-6">

                        
                        <div className="flex items-center justify-between">
                            <div>
                                <p className="text-sm text-gray-500">Market Overview</p>
                                <p className="mt-1 text-2xl font-bold text-gray-900">
                                    $184.32
                                </p>
                            </div>

                            <span className="rounded-md bg-gray-200 px-3 py-1 text-sm font-medium text-gray-700">
                                +4.82%
                            </span>
                        </div>

                        {/* chart */}
                        <div className="mt-8 flex h-64 items-end gap-2 rounded-xl border border-gray-200 bg-white p-4">

                            <div className="h-[30%] w-full rounded-t bg-gray-300" />
                            <div className="h-[40%] w-full rounded-t bg-gray-400" />
                            <div className="h-[35%] w-full rounded-t bg-gray-300" />
                            <div className="h-[52%] w-full rounded-t bg-gray-400" />
                            <div className="h-[47%] w-full rounded-t bg-gray-300" />
                            <div className="h-[63%] w-full rounded-t bg-gray-400" />
                            <div className="h-[58%] w-full rounded-t bg-gray-300" />
                            <div className="h-[73%] w-full rounded-t bg-gray-500" />
                            <div className="h-[68%] w-full rounded-t bg-gray-400" />
                            <div className="h-[84%] w-full rounded-t bg-gray-500" />
                            <div className="h-[78%] w-full rounded-t bg-gray-400" />
                            <div className="h-[92%] w-full rounded-t bg-gray-600" />

                        </div>

                        {/* Prediction box */}
                        <div className="mt-4 flex items-center justify-between rounded-xl bg-black px-4 py-4 text-white">
                            <div>
                                <p className="text-xs text-gray-300">
                                    AI Prediction
                                </p>
                                <p className="mt-1 text-sm font-semibold">
                                    Positive trend detected
                                </p>
                            </div>

                            <span className="text-xl">↗</span>
                        </div>
                    </div>
                </div>

            </div>
        </section>
    );
}

export default Hero;