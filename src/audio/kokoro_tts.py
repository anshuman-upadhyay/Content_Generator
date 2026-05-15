from pathlib import Path
import soundfile as sf
from kokoro_onnx import Kokoro
import gc


OUTPUT_PATH = Path("temp/narration.wav")
MODEL_PATH = Path("models/kokoro-v1.0.onnx")
VOICES_PATH = Path("models/voices-v1.0.bin")


def generate_kokoro_tts(script):
    """
    Generate narration using Kokoro ONNX
    """

    if not script.strip():
        raise ValueError("Script is empty")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Kokoro model file not found in models/"
        )

    if not VOICES_PATH.exists():
        raise FileNotFoundError(
            "Kokoro voices file not found in models/"
        )

    try:
        print("Loading Kokoro model...")

        model = Kokoro(
            model_path=str(MODEL_PATH),
            voices_path=str(VOICES_PATH)
        )

        print("Generating narration...")

        audio, sample_rate = model.create(
            text=script,
            voice="af_bella",
            speed=1.0
        )

        OUTPUT_PATH.parent.mkdir(exist_ok=True)

        sf.write(
            str(OUTPUT_PATH),
            audio,
            sample_rate
        )

        print(f"Narration saved at {OUTPUT_PATH}")

        # cleanup memory
        del model
        del audio
        gc.collect()

        print("Kokoro memory cleaned successfully.")

    except Exception as e:
        raise RuntimeError(
            f"Kokoro TTS generation failed: {e}"
        )


if __name__ == "__main__":
    print("Run this through content pipeline")