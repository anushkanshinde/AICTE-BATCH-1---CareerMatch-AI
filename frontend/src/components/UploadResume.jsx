import { useState } from "react";
import axios from "axios";
import { saveAs } from "file-saver";

function UploadResume() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a resume");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData,
      );

      setResults(response.data);
    } catch (error) {
      console.error(error);

      if (error.response) {
        alert(JSON.stringify(error.response.data));
      } else {
        alert(error.message);
      }
    } finally {
      setLoading(false);
    }
  };

  const downloadReport = async () => {
    if (!file) {
      alert("Please upload a resume first");
      return;
    }

    try {
      const formData = new FormData();

      formData.append("file", file);

      const response = await axios.post(
        "http://127.0.0.1:8000/download-report",
        formData,
        {
          responseType: "blob",
        },
      );

      saveAs(response.data, "CareerMatch_Report.pdf");
    } catch (error) {
      console.error(error);

      alert("Failed to download report");
    }
  };

  return (
    <div>
      {/* Upload Section */}

      <div className="flex flex-col items-center gap-4">
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
          className="border p-3 rounded-lg"
        />

        <div className="flex gap-4">
          <button
            onClick={uploadResume}
            className="
              bg-blue-600
              text-white
              px-6
              py-3
              rounded-xl
              hover:bg-blue-700
            "
          >
            Analyze Resume
          </button>

          <button
            onClick={downloadReport}
            className="
              bg-green-600
              text-white
              px-6
              py-3
              rounded-xl
              hover:bg-green-700
            "
          >
            Download Report
          </button>
        </div>
      </div>

      {/* Loading */}

      {loading && (
        <div className="text-center mt-8">
          <h3 className="text-lg font-semibold">Analyzing Resume...</h3>
        </div>
      )}

      {/* Results */}

      {results && (
        <div className="mt-10 space-y-8">
          {/* Best Match */}

          <div
            className="
            bg-blue-600
            text-white
            p-6
            rounded-2xl
            text-center
            shadow-lg
          "
          >
            <h2 className="text-xl">Best Career Match</h2>

            <h1 className="text-4xl font-bold mt-2">
              {results.career_prediction}
            </h1>
          </div>

          {/* Detected Skills */}

          <div>
            <h3 className="text-2xl font-bold mb-3">Detected Skills</h3>

            <div className="flex flex-wrap gap-2">
              {results.detected_skills.map((skill) => (
                <span
                  key={skill}
                  className="
                      bg-green-100
                      text-green-800
                      px-3
                      py-2
                      rounded-full
                      text-sm
                      font-medium
                    "
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>

          {/* Missing Skills */}

          <div>
            <h3 className="text-2xl font-bold mb-3">Recommended Skills</h3>

            <div className="flex flex-wrap gap-2">
              {results.missing_skills.map((skill) => (
                <span
                  key={skill}
                  className="
                      bg-red-100
                      text-red-800
                      px-3
                      py-2
                      rounded-full
                      text-sm
                      font-medium
                    "
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>

          {/* AI Career Advice */}

          <div>
            <h3 className="text-2xl font-bold mb-3">AI Career Advice</h3>

            <div
              className="
                bg-gray-100
                p-5
                rounded-xl
                whitespace-pre-wrap
                leading-7
              "
            >
              {results.career_advice}
            </div>
          </div>

          {/* Similarity Scores */}

          <div>
            <h3 className="text-2xl font-bold mb-4">Career Scores</h3>

            {Object.entries(results.similarity_scores).map(([role, score]) => (
              <div key={role} className="mb-5">
                <div
                  className="
                      flex
                      justify-between
                      mb-1
                    "
                >
                  <span>{role}</span>

                  <span>{score}%</span>
                </div>

                <div
                  className="
                      w-full
                      bg-gray-200
                      rounded-full
                      h-4
                    "
                >
                  <div
                    className="
                        bg-blue-600
                        h-4
                        rounded-full
                      "
                    style={{
                      width: `${score}%`,
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default UploadResume;
