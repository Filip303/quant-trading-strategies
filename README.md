# Quant Trading Strategies

Notebooks de Python para investigar reglas de trading con datos históricos. La colección incluye reversión a la media, momentum y modelos de régimen de mercado.

## Estrategias

| Notebook | Idea | Datos |
| --- | --- | --- |
| [Bandas de Bollinger y RSI](notebooks/bollinger-rsi.ipynb) | Combina ambos indicadores para buscar reversiones a la media. | FMP |
| [IBS y ROC](notebooks/ibs-roc.ipynb) | Usa la posición del cierre en el rango diario y la tasa de cambio del precio. Incluye dos variantes. | FMP |
| [IBS y medias móviles exponenciales](notebooks/ibs-ema.ipynb) | Combina el cierre dentro del rango diario con filtros de tendencia EMA. | Yahoo Finance |
| [Momentum de series temporales](notebooks/tsmom.ipynb) | Usa la tendencia del activo para definir la señal y ajusta la exposición según la volatilidad. | FMP |
| [Regímenes con mezcla gaussiana](notebooks/gmm-regimes.ipynb) | Reestima el modelo de regímenes en ventanas sucesivas y simula las señales de cada tramo. | FMP |
| [Regímenes por umbrales de volatilidad](notebooks/volatility-threshold-regimes.ipynb) | Estima la volatilidad Yang–Zhang y aplica umbrales móviles con validación walk-forward. | FMP |
| [Asignación por HMM y semivarianza](notebooks/hmm-semivariance-allocation.ipynb) | Estima regímenes con un modelo oculto de Márkov y ajusta la asignación de cartera según el régimen. | FMP |
| [XGBoost adaptativo al régimen](notebooks/xgboost-regime-adaptive.ipynb) | Combina XGBoost con un modelo de regímenes y recalibra los umbrales de entrada y salida en cada ventana. | FMP |

## Ejecutar los notebooks

Con Python 3.13, instala las dependencias en un entorno virtual desde la raíz del repositorio.

```bash
python -m venv .venv
```

Activa el entorno con el comando de tu sistema.

- macOS y Linux usan `source .venv/bin/activate`.
- PowerShell usa `.\.venv\Scripts\Activate.ps1`.

```bash
python -m pip install -r requirements.txt
```

Para los notebooks de Financial Modeling Prep (FMP), define `FMP_API_KEY` antes de iniciar Jupyter. Tu cuenta debe tener acceso a los símbolos y al rango histórico que configura cada notebook. [Documentación del endpoint histórico de FMP](https://site.financialmodelingprep.com/developer/docs/stable/historical-price-eod-full)

```bash
# macOS y Linux
export FMP_API_KEY='tu_clave'
```

```powershell
# Windows PowerShell
$env:FMP_API_KEY = 'tu_clave'
```

Inicia `python -m jupyterlab`, abre el notebook y ejecuta las celdas en orden. El notebook de Yahoo Finance descarga los datos sin clave. Algunos notebooks escriben CSV o gráficos en el directorio de ejecución o en `results/`. Los supuestos de costes, fechas y ejecución varían entre estrategias.
