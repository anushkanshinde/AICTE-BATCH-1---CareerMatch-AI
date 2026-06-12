import UploadResume from "./components/UploadResume";

function App() {
  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-8">
      <div className="bg-white w-full max-w-4xl rounded-3xl shadow-2xl p-10">
        <h1 className="text-5xl font-bold text-center text-slate-800">
          CareerMatch AI
        </h1>

        <p className="text-center text-gray-500 mt-4">
          AI Powered Resume Career Analyzer
        </p>

        <div className="mt-10">
          <UploadResume />
        </div>
      </div>
    </div>
  );
}

export default App;
